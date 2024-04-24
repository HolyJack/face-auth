import { Card, CardBody, CardHeader } from "@nextui-org/card";
import CustomWebcam from "./CustomWebcam";
import { useState } from "react";
import { Button } from "@nextui-org/button";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";

function Login() {
  const [imgSrc, setImgSrc] = useState(null);
  const [username, setUsername] = useState(null);
    const mutation = useMutation({ mutationFn: ({ imgSrc }) => {
        return axios.post("http://localhost:40/retrieve", { imgSrc }).then(res => setUsername(res.data))
    } })

    function onSubmit(e) {
        e.preventDefault()
        mutation.mutate({ imgSrc })
    }

  return (
  <Card className="container">
    <CardHeader>
      <h2 className="text-center text-xl font-semibold">Login</h2>
    </CardHeader>
    <CardBody className="flex flex-col gap-2">
      <Card>
        <CardBody className="w-full">You are: {username}</CardBody>
      </Card>
      <form onSubmit={onSubmit}>
      <CustomWebcam imgSrc={imgSrc} setImgSrc={v => setImgSrc(v)}/>
      <Button color="success" isLoading={mutation.isPending} className="mt-6" type="submit" isDisabled={!imgSrc}>Submit</Button>
      </form>
    </CardBody>
  </Card>
  )
}

export default Login;