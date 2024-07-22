import React from "react";

const FeaturesList = () => {
  return (
    <ul className="list-disc ml-3 mt-4">
      <li>Get verses from the Quran in JSON format</li>
      <li>Get JSON of a whole surah</li>
      <li>
        Get{" "}
        <code className="text-xs md:text-sm bg-gray-800 px-1 py-0.5 rounded-md border border-gray-700 bg-opacity-60">
          mp3
        </code>{" "}
        files of each verse
      </li>
    </ul>
  );
};

export default FeaturesList;
