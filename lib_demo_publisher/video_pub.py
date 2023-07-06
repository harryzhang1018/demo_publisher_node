import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class VideoPublisher(Node):

    def __init__(self, video_path, topic_name, frame_rate):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, topic_name, 10)
        self.timer_ = self.create_timer(1.0 / frame_rate, self.publish_frame)
        self.bridge = CvBridge()

        self.video = cv2.VideoCapture(video_path)
        self.get_logger().info('Video read completed.')
        if not self.video.isOpened():
            raise Exception("Failed to open the video file.")

    def publish_frame(self):
        self.get_logger().info('Video is being published')
        ret, frame = self.video.read()

        if not ret:
            self.video.release()
            self.get_logger().info('Video publishing completed.')
            self.timer_.cancel()
            return

        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(msg)


def main():
    rclpy.init()

    video_path = "/home/videos/test.mp4"
    topic_name = "/demo_video"
    frame_rate = 10  # Adjust the frame rate as desired

    video_publisher = VideoPublisher(video_path, topic_name, frame_rate)

    rclpy.spin(video_publisher)

    video_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
