import React from "react";

const FeaturesList = () => {
  return (
    <ul className="list-disc ml-3 mt-4">
      <li>Get verses from the Quran in JSON format</li>
      <li>Get JSON of a whole surah</li>
      <li>
        Get{" "}
        <span className="font-mono text-xs md:text-sm font-semibold">mp3</span>{" "}
        files of each verse
      </li>
    </ul>
  );
};

export default FeaturesList;
