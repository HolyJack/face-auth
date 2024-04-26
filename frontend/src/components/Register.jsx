import { Card, CardBody, CardHeader } from "@nextui-org/card";
import CustomWebcam from "./CustomWebcam";
import {Button, Input} from "@nextui-org/react";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";

function Register() {
  const [username, setUsername] = useState("");
  const [imgSrc, setImgSrc] = useState(null);

  const mutation = useMutation({mutationFn: ({ username, imgSrc }) =>
      { return axios.post("/register", { login: username, img: imgSrc }) }})

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
      <form onSubmit={onSubmit} className="flex flex-col gap-2">
        <Input className="h-14" label="Username" value={username} onChange={e => setUsername(e.target.value)}></Input>
        <CustomWebcam imgSrc={imgSrc} setImgSrc={v => setImgSrc(v)}/>
        <Button color="success" className="mt-2" type="submit" isLoading={mutation.isPending} isDisabled={!imgSrc || !username}>Submit</Button>
      </form>
    </CardBody>
  </Card>
  );
}

export default Register
