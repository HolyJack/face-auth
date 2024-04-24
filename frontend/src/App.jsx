import { Tab, Tabs } from "@nextui-org/tabs";
import Login from "./components/Login";
import Register from "./components/Register";
import HowItWorks from "./components/HowItWorks";

function App() {
  return (
    <div>
      <header className="flex justify-center border-b p-4">
      <h1 className="text-4xl">Face Recognition Auth</h1></header>
      <main className="container mx-auto">
        <div className="mx-auto my-2 flex max-w-screen-md flex-col">
          <Tabs aria-label="Options">
            <Tab key="howitworks" title="How it works?">
              <HowItWorks />
            </Tab>
            <Tab key="register" title="Register">
              <Register />
            </Tab>
            <Tab key="login" title="Login">
              <Login />
            </Tab>
          </Tabs>
        </div>
      </main>
    </div>
  );
}

export default App;
