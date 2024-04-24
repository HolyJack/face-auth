import { useCallback, useRef } from "react";
import { Button } from "@nextui-org/button";
import Webcam from "react-webcam";

function CustomWebcam({imgSrc, setImgSrc}) {
  const ref = useRef();
    const capture = useCallback(() => {
        const imageSrc = ref.current.getScreenshot();
        setImgSrc(imageSrc);
    }, [ref, setImgSrc])

    const retake = () => {
        setImgSrc(null);
    }

  return (
      <div className="flex max-w-screen-md flex-col gap-2">
      <div className="flex h-[450px] justify-center rounded-md border bg-black object-contain">
      {imgSrc ? (
        <img src={imgSrc} alt="webcam" />
      ) : (
        <Webcam ref={ref} />
      )}
      </div>
      <div className="flex justify-evenly gap-2 ">
          <Button className="flex-1" color="default" onClick={retake} isDisabled={!imgSrc}>Retake photo</Button>
          <Button className="flex-1" color="primary" onClick={capture} isDisabled={imgSrc}>Capture photo</Button>
      </div>
      </div>
  );
}

export default CustomWebcam;
