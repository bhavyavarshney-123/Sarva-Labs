// SPDX-License-Identifier: MIT
pragma solidity ^0.4.18;
contract Owned {
    address owner;
    
    constructor() public{
        owner = msg.sender;
    }
    
   modifier onlyOwner {
       require(msg.sender == owner);
       _;
   }
}

contract AttendanceSheet is Owned  {
   
    struct Student {
        uint Age;
        string FirstName;
        string LastName;
        uint AttendanceValue;    
    }
    mapping (uint => Student) StudentList;
    uint[] public StudentIdList;
    
    event studentCreationEvent(
       string FirstName,
       string LastName,
       uint Age
    );
    
    function createStudent(uint _StudentId, uint _Age, string _FirstName, string _LastName) onlyOwner public {
        var student = StudentList[_StudentId];
        
        student.Age = _Age;
        student.FirstName = _FirstName;
        student.LastName = _LastName;
        student.AttendanceValue = 0;
        StudentIdList.push(_StudentId) -1;
       emit studentCreationEvent(_FirstName, _LastName, _Age);
    }
    
    function incrementAttendance(uint _StudentId) onlyOwner public {
        StudentList[_StudentId].AttendanceValue = StudentList[_StudentId].AttendanceValue+1;
    }
    
    function getStudents() view public returns(uint[]) {
      return StudentIdList;
    }
    
    function getParticularStudent(uint _StudentId) public view returns (string, string, uint, uint) {
        return (StudentList[_StudentId].FirstName, StudentList[_StudentId].LastName, StudentList[_StudentId].Age, StudentList[_StudentId].AttendanceValue);
    }

    function countStudents() view public returns (uint) {
        return StudentIdList.length;
    }
}
