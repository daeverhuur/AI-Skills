# Media Generation

## Table of Contents
- [Nano Banana / Imagen 4](#nano-banana--imagen-4)
- [Veo 3 / Veo 3.1](#veo-3--veo-31)
- [Pomelli](#pomelli)
- [Mixboard](#mixboard)
- [Lyria 2 (Music)](#lyria-2)

## Nano Banana / Imagen 4

Google's state-of-the-art image generation and editing model. Integrated into Gemini app, AI Studio, and available via API.

**Generation capabilities**:
- Text-to-image with natural language prompts
- Photorealistic, illustration, painting, neon, sketch styles
- Text rendering in images (logos, posters, infographics, memes)
- Character consistency: same person/character across multiple generations
- Multi-image fusion: combine elements from multiple input images
- High resolution output

**Editing capabilities** (upload image + describe changes):
- Background replacement (lighting/shadows adjust automatically)
- Object removal with intelligent inpainting
- Style transfer (change art style, preserve content)
- Local edits: color changes, blur, add/remove elements
- Pose alteration (change how people are positioned)
- Black & white to color restoration
- Clothing/accessory changes
- Scene composition changes

**API usage**:
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")  # or pro

# Generate image
response = model.generate_content("Generate an image of a cat wearing a top hat in a steampunk style")

# Edit image
image = genai.upload_file("photo.jpg")
response = model.generate_content(["Make the background a sunset beach", image])
```

**Key advantages over competitors**:
- Best text rendering of any image model
- Superior character consistency across generations
- Natural multi-image editing (maintains context across edits in chat)
- Integrated with Gemini's language understanding
- 10 million users joined Gemini in one week due to Nano Banana

**Use cases**: Product photography, social media content, marketing materials, meme creation, photo restoration, brand assets, thumbnail generation

## Veo 3 / Veo 3.1

Google's video generation models. Industry-leading quality.

**Veo 3**:
- Text-to-video generation
- Native audio generation (dialogue, sound effects, ambient sound)
- First AI video model with synchronized audio
- Up to 1080p resolution

**Veo 3.1** (released October 2025):
- Resolutions: 720p, 1080p, or 4K
- Duration: up to 60 seconds per clip
- Improved quality, motion physics, and character consistency
- Multi-reference-image input (direct characters, objects, scene style)
- Video extension: extend previously generated clips
- Frame-specific generation: specify first and/or last frames
- Enhanced prompt adherence
- Vertical video support for social media

**Veo 3 Fast**:
- Optimized for speed
- Available free on YouTube Shorts
- Quick generation for social media content

**Input modes**:
- Text-to-video: describe the scene in natural language
- Image-to-video: animate a still image
- Video-to-video: modify existing video clips

**Available in**:
- Gemini app (Pro/Ultra plans)
- YouTube Shorts (Veo 3 Fast, free for creators)
- AI Studio (via API)
- Vertex AI (enterprise)

**YouTube Shorts integration**:
- Generate short video clips with sound from text prompts
- Animate people in photos
- "Edit with AI" analyzes camera roll footage and pairs with music/effects
- Speech-to-song (remix quotes from videos into songs via Lyria 2)

**Use cases**: Social media content, product demos, promotional videos, storyboarding, concept visualization, UGC-style ad generation

## Pomelli

Google's on-brand animation tool powered by Veo 3.1.

**Key features**:
- Upload brand assets (logos, characters, products)
- Generate branded animations maintaining brand consistency
- Motion graphics and animated content
- Customizable style, mood, and pacing
- Export for social media, presentations, ads

**Best for**: Brand-consistent animated content, social media animations, product animations

## Mixboard

AI-powered presentation and visual board tool.

**Key features**:
- Create presentations and visual boards with AI assistance
- Uses Nano Banana for generating presentation visuals
- AI-generated layouts and designs
- Collaborative editing
- Export to standard presentation formats

**Best for**: Quick presentation creation, visual brainstorming, mood boards, marketing collateral

## Lyria 2

Google's music generation model.

**Capabilities**:
- Text-to-music generation
- Speech-to-song (convert spoken words into musical tracks)
- Multiple genres and styles
- Integrated into YouTube Shorts for creators

**YouTube integration**: Creators can take quotes from videos and remix them into catchy songs for Shorts content.
