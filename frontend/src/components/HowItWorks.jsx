import { Card, CardBody, CardHeader } from "@nextui-org/card";

function HowItWorks() {
  return (
  <Card className="container">
    <CardHeader>
      <h2 className="text-center text-xl font-semibold">How it works?</h2>
    </CardHeader>
    <CardBody>
    1. Register an account<br />
    1.1 Select a username<br />
    1.2 Take a photo<br />
    1.3 Click on the register button<br />
    <br />
    2. Go to Login<br />
    2.1 Take a photo<br />
    2.2 Get your username!<br />
    </CardBody>
  </Card>
  )
}

export default HowItWorks;
