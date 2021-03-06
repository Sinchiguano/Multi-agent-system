// Generated by gencpp from file robot_coordination/StopMovementRequest.msg
// DO NOT EDIT!


#ifndef ROBOT_COORDINATION_MESSAGE_STOPMOVEMENTREQUEST_H
#define ROBOT_COORDINATION_MESSAGE_STOPMOVEMENTREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robot_coordination
{
template <class ContainerAllocator>
struct StopMovementRequest_
{
  typedef StopMovementRequest_<ContainerAllocator> Type;

  StopMovementRequest_()
    {
    }
  StopMovementRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::robot_coordination::StopMovementRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot_coordination::StopMovementRequest_<ContainerAllocator> const> ConstPtr;

}; // struct StopMovementRequest_

typedef ::robot_coordination::StopMovementRequest_<std::allocator<void> > StopMovementRequest;

typedef boost::shared_ptr< ::robot_coordination::StopMovementRequest > StopMovementRequestPtr;
typedef boost::shared_ptr< ::robot_coordination::StopMovementRequest const> StopMovementRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot_coordination::StopMovementRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robot_coordination

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'robot_coordination': ['/home/casch/turtle/src/mkr2018_mrc/robot_coordination/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot_coordination::StopMovementRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_coordination::StopMovementRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_coordination::StopMovementRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::robot_coordination::StopMovementRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot_coordination/StopMovementRequest";
  }

  static const char* value(const ::robot_coordination::StopMovementRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::robot_coordination::StopMovementRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StopMovementRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot_coordination::StopMovementRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::robot_coordination::StopMovementRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_COORDINATION_MESSAGE_STOPMOVEMENTREQUEST_H
