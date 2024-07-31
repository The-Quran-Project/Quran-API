const Hero = () => {
  return (
    <main className="pb-10 text-center">
      <header className="md:text-6xl lg:text-7xl font-bold mt-10 mb-5 text-4xl scale-110">
        Quran for Everyone
      </header>
      <span className="font-semibold font-mono mb-12 block text-sm md:text-base  scale-95 md:scale-100 opacity-70">
        API for the Quran with no rate limit. No authentication required
      </span>
      <span className="center">
        <a className="styled-button" href="/introduction">
          Docs →
        </a>
      </span>
    </main>
  );
};

// change theme to `class` instead of system preferences

export default Hero;
