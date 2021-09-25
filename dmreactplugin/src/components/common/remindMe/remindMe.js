import React, { useState } from "react";
import { Button, Form, FormGroup, Label, Input } from "reactstrap";
import { DatePicker, TimePicker } from "react-rainbow-components";
import './remindMe.css'

const RemindMe = () => {
  const [date, setDate] = useState(null);

  function onChange(date) {
    setDate(date);
  }
  return (
    <div className="dm-remind-me-wrapper">
      <Form className="dm-remind-me">
        <h3 className="dm-remind-me-header">Create a reminder</h3>
        <FormGroup className="dm-date-wrapper">
          <Label for="date" classname="dm-labels">Date</Label>
          <DatePicker
            id="datePicker-1"
            value={date}
            onChange={onChange}
            label=""
            formatStyle="large"
          />
        </FormGroup>
        <FormGroup className="dm-time-wrapper">
          <Label for="time" classname="dm-labels">Time</Label>
          <TimePicker
            id="datePicker-1"
            value={date}
            onChange={onChange}
            label=""
            formatStyle="large"
          />
        </FormGroup>
        <FormGroup className="dm-note-wrapper">
          <Label for="note" classname="dm-labels">
            Add a note<em>(optional)</em>
          </Label>
          <Input type="textarea" name="text" id="exampleText" />
        </FormGroup>
        <FormGroup className="dm-button-wrapper">
          <Button className="dm-cancel">Cancel</Button>
          <Button className="dm-create">Create</Button>
        </FormGroup>
      </Form>
    </div>
  );
};

export default RemindMe;
