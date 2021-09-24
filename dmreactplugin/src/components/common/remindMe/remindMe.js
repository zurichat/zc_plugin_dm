import React, { useState } from "react";
import { Button, Form, FormGroup, Label, Input } from "reactstrap";
import { DatePicker, TimePicker } from "react-rainbow-components";
import './RemindMe.css'

const RemindMe = () => {
  const [date, setDate] = useState(null);

  function onChange(date) {
    setDate(date);
  }
  return (
    <div className="remind-me-wrapper">
      <Form className="remind-me">
        <h3 className="remind-me-header">Create a reminder</h3>
        <FormGroup className="date-wrapper">
          <Label for="date">Date</Label>
          <DatePicker
            id="datePicker-1"
            value={date}
            onChange={onChange}
            label=""
            formatStyle="large"
          />
        </FormGroup>
        <FormGroup className="time-wrapper">
          <Label for="time">Time</Label>
          <TimePicker
            id="datePicker-1"
            value={date}
            onChange={onChange}
            label=""
            formatStyle="large"
          />
        </FormGroup>
        <FormGroup className="note-wrapper">
          <Label for="note">
            Add a note<em>(optional)</em>
          </Label>
          <Input type="textarea" name="text" id="exampleText" />
        </FormGroup>
        <FormGroup className="button-wrapper">
          <Button className="cancel">Cancel</Button>
          <Button className="create">Create</Button>
        </FormGroup>
      </Form>
    </div>
  );
};

export default RemindMe;
