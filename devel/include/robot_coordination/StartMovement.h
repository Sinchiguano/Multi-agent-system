// Generated by gencpp from file robot_coordination/StartMovement.msg
// DO NOT EDIT!


#ifndef ROBOT_COORDINATION_MESSAGE_STARTMOVEMENT_H
#define ROBOT_COORDINATION_MESSAGE_STARTMOVEMENT_H

#include <ros/service_traits.h>


#include <robot_coordination/StartMovementRequest.h>
#include <robot_coordination/StartMovementResponse.h>


namespace robot_coordination
{

struct StartMovement
{

typedef StartMovementRequest Request;
typedef StartMovementResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct StartMovement
} // namespace robot_coordination


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robot_coordination::StartMovement > {
  static const char* value()
  {
    return "8f5729177853f34b146e2e57766d4dc2";
  }

  static const char* value(const ::robot_coordination::StartMovement&) { return value(); }
};

template<>
struct DataType< ::robot_coordination::StartMovement > {
  static const char* value()
  {
    return "robot_coordination/StartMovement";
  }

  static const char* value(const ::robot_coordination::StartMovement&) { return value(); }
};


// service_traits::MD5Sum< ::robot_coordination::StartMovementRequest> should match 
// service_traits::MD5Sum< ::robot_coordination::StartMovement > 
template<>
struct MD5Sum< ::robot_coordination::StartMovementRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robot_coordination::StartMovement >::value();
  }
  static const char* value(const ::robot_coordination::StartMovementRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robot_coordination::StartMovementRequest> should match 
// service_traits::DataType< ::robot_coordination::StartMovement > 
template<>
struct DataType< ::robot_coordination::StartMovementRequest>
{
  static const char* value()
  {
    return DataType< ::robot_coordination::StartMovement >::value();
  }
  static const char* value(const ::robot_coordination::StartMovementRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robot_coordination::StartMovementResponse> should match 
// service_traits::MD5Sum< ::robot_coordination::StartMovement > 
template<>
struct MD5Sum< ::robot_coordination::StartMovementResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robot_coordination::StartMovement >::value();
  }
  static const char* value(const ::robot_coordination::StartMovementResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robot_coordination::StartMovementResponse> should match 
// service_traits::DataType< ::robot_coordination::StartMovement > 
template<>
struct DataType< ::robot_coordination::StartMovementResponse>
{
  static const char* value()
  {
    return DataType< ::robot_coordination::StartMovement >::value();
  }
  static const char* value(const ::robot_coordination::StartMovementResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOT_COORDINATION_MESSAGE_STARTMOVEMENT_H
