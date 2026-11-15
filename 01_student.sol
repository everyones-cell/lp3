// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    struct Student {
        uint id;
        string name;
        uint8 age;
        string course;
    }

    Student[] students;

    function addStudent(uint id, string memory name, uint8 age, string memory course) public {
        students.push(Student(id, name, age, course));
    }

    function getStudent(uint i) public view returns (uint, string memory, uint8, string memory) {
        require(i < students.length, "Invalid index");
        Student memory s = students[i];
        return (s.id, s.name, s.age, s.course);
    }

    function getTotalStudents() public view returns (uint) {
        return students.length;
    }

    event FallbackCalled(address sender, uint value);
event ReceiveCalled(address sender, uint value);

fallback() external payable {
    emit FallbackCalled(msg.sender, msg.value);
}

receive() external payable {
    emit ReceiveCalled(msg.sender, msg.value);
}
}
