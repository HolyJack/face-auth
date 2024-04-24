import { Card, CardBody, CardHeader } from "@nextui-org/card";
import CustomWebcam from "./CustomWebcam";
import {Button, Input} from "@nextui-org/react";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";

function Register() {
  const [username, setUsername] = useState("");
  const [imgSrc, setImgSrc] = useState(null);

  const mutation = useMutation({ name: "register" , mutationFn: ({ username, imgSrc }) =>
      { return axios.post("http://localhost:40/register", { username, imgSrc }) }})

    function onSubmit(e) {
        e.preventDefault()
        mutation.mutate({ username, imgSrc})
    }

  return (
  <Card>
    <CardHeader>
      <h2 className="text-center text-xl font-semibold">Registration</h2>
    </CardHeader>
    <CardBody className="flex flex-col gap-2">
      <form onSubmit={onSubmit}>
      <Input label="Username" value={username} onChange={e => setUsername(e.target.value)}></Input>
      <CustomWebcam imgSrc={imgSrc} setImgSrc={v => setImgSrc(v)}/>
      <Button color="success" className="mt-6" type="submit" isLoading={mutation.isPending} isDisabled={!imgSrc || !username}>Submit</Button>
      </form>
    </CardBody>
  </Card>
  );
}

export default Register
