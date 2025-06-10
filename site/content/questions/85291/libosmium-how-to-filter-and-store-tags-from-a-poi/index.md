+++
type = "question"
title = "Libosmium - How to filter and store tags from a POI?"
description = '''Hi  I&#x27;m new to OSM and Libosmium. My goal is to filter certain POI e.g. all the libraries worldwide with the location and certain tags and store it as a json to later processing (e.g. search nearest library). As source file sI use OSM extracts from http://download.geofabrik.de/ To be able to process...'''
date = "2022-08-09T13:08:00Z"
lastmod = "2022-08-10T17:14:00Z"
weight = 85291
keywords = [ "libosmium", "json", "store" ]
aliases = [ "/questions/85291" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Libosmium - How to filter and store tags from a POI?](/questions/85291/libosmium-how-to-filter-and-store-tags-from-a-poi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85291-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm new to OSM and Libosmium. My goal is to filter certain POI e.g. all the libraries worldwide with the location and certain tags and store it as a json to later processing (e.g. search nearest library). As source file sI use OSM extracts from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a></p>
<p>To be able to process it locally I started to look into Libosmium even though I'm a newbie with cpp. I'm using Ubuntu 20.04 and was able to compile Libosmium (which was already great). Under /examples/ I found a pretty close example <code>osmium_amenity_list.cpp</code> <a href="https://github.com/osmcode/libosmium/blob/master/examples/osmium_amenity_list.cpp">https://github.com/osmcode/libosmium/blob/master/examples/osmium_amenity_list.cpp</a> which I want to adop to my needs. Could someone please help me with the following:</p>
<p>1) How can I filter on <code>amenity=library</code>? My current solution:</p>
<pre><code>const char *amenity_type = node.tags()[&quot;amenity&quot;];
if (amenity_type)
{
    if (strcmp(amenity_type, &quot;library&quot;) == 0)
    {...</code></pre>
<p>Is there a way to query amentiy=libray within the first line?</p>
<pre><code>const char *amenity_type = node.tags()[&quot;amenity&quot;];</code></pre>
<p>2) Is there a way to loop through all available fields e.g. for nodes I want to extract as well not only "name" + "location (lat, lon)", but also e.g. id, addr:country, addr:city, addr:street, addr:housenumber, ...</p>
<p>3) Instead of printf() of <code>print_amenity()</code> I want to store it as json file. I'm still new to cpp (I'm more familiar with python, where I would e.g. store each entry as a dict() within a list() and later convert the list into a json or dataframe). e.g. I would like to query later either with cpp or python the json for the closest libraries within a certain range via haversine.</p>
<p>-&gt; How would I adopt it to instead of print store it in a json or similar format? What I found was e.g. the proposal to use a map in combination with a tuple and a vector.</p>
<pre><code>#include &lt;map&gt;
#include &lt;tuple&gt;
#include &lt;vector&gt;
using KeyType = std::tuple&lt;int, int&gt;;
using ValueType = std::vector&lt;KeyType&gt;;
std::map&lt;KeyType, ValueType&gt; Nodes;</code></pre>
<p>Not sure if this is the best way to be used with Libosmium (or put different how should I replace <code>print_amenity()</code> to be able to store and later further process it)?</p>
<p>Thank you very much</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-libosmium" rel="tag" title="see questions tagged &#39;libosmium&#39;">libosmium</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-store" rel="tag" title="see questions tagged &#39;store&#39;">store</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '22, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a8584e178b3c216a8d75fc32ac58a095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muran123&#39;s gravatar image" />
<p><span>Muran123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muran123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '22, 10:29</strong> </span></p>
</div>
</div>
<div id="comments-container-85291" class="comments-container">
&#10;</div>
<div id="comment-tools-85291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85291-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="85298"></span>

<div id="answer-container-85298" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85298-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Rather than learning C++ for this project and especially because you are already familiar with Python I suggest the following approach: Use the <a href="https://osmcode.org/osmium-tool/">osmium command line tool</a> to do a rough filtering of the input, for instance with <code>osmium tags-filter input.osm.pbf n/amenity=library -o output.osm.pbf</code>. This will give you an OSM file with only those nodes that have a tag <code>amenity=library</code> which is much much smaller than what you had before and because Osmium is written in C++ it is quite fast. After that use <a href="https://osmcode.org/pyosmium/">PyOsmium</a> for the rest, more detailed filtering, conversion to JSON or whatever else you want to do. It will be a bit slower than processing in C++, but development will be much easier.</p>
<p>To answer your questions (somewhat): 1. The approach you are using is correct, 2. You can loop over all tags with <code>for (auto const &amp;tag : node.tags()) {...}</code>. 3. You'll need a JSON library, it depends on the library how best to drive that. The answer to that goes well beyond something I can answer quickly here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '22, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-85298" class="comments-container">
&#10;</div>
<div id="comment-tools-85298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85298-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85308"></span>

<div id="answer-container-85308" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85308-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/users/112/jochen-topf"></a><a href="https://help.openstreetmap.org/users/112/jochen-topf">@Jochen</a></a>: Thank you very much for your answer. I like you proposed approach and I followed on it.</p>
<p>a) Thanks to the amazing "osmium command line tool" I was able to quickly filter the pbf file for amenity=library (I only extended the filter to also include ways and relations with "nwr/" instead of "n/" only for nodes.</p>
<p>b) For the further processing I already tried to use PyOsium before and was struggling to get it working to extract tags and store them (<a href="https://github.com/osmcode/pyosmium/issues/208">https://github.com/osmcode/pyosmium/issues/208</a>). I was trying to follow the recommendations in <a href="https://github.com/osmcode/pyosmium/blob/master/doc/intro.rst">https://github.com/osmcode/pyosmium/blob/master/doc/intro.rst</a> but I keep getting <em>"RuntimeError: Node callback keeps reference to OSM object. This is not allowed."</em> That's the reason why I started to try to do it with Libosmium, because I was stuck with this error in python. When I try to run it with the following python program (which is a copy of the example from <a href="https://github.com/osmcode/pyosmium/blob/master/doc/intro.rst">2</a> like mentioned in the github issue <a href="https://github.com/osmcode/pyosmium/issues/208">1</a>, adopted for "amenity=library" and with the file <a href="http://download.geofabrik.de/europe/germany-latest.osm.pbf">http://download.geofabrik.de/europe/germany-latest.osm.pbf</a> from Geofabrik.</p>
<pre><code>import osmium
from pathlib import Path
&#10;class HotelHandler(osmium.SimpleHandler):
    def __init__(self):
        super(HotelHandler, self).__init__()
        self.hotels = []
&#10;    def node(self, o):
        if o.tags.get(&#39;amenity&#39;) == &#39;library&#39; and &#39;name&#39; in o.tags:
            print(str(o.tags[&#39;name&#39;]))
            self.hotels.append(o.tags[&#39;name&#39;])
&#10;def main():
    data_file = Path(&#39;/home/..../germany-latest.osm.pbf&#39;)
    h = HotelHandler()
    h.apply_file(data_file)
&#10;    print(sorted(h.hotels))
&#10;main()</code></pre>
<p>I get the first 2 entries</p>
<p>Stadtbibliothek Weinheim</p>
<p>Deutsche Nationalbibliothek</p>
<p>appended to the list (and also print out) and afterwards the program stops with <em>"Node callback keeps reference to OSM object. This is not allowed."</em></p>
<p>My technical set-up: Ubuntu 20.04, Python 3.8.10, IDE PyCharm 2022.2</p>
<p>May I ask you, if you could help me with what is going wrong in the python program? Thank you very much</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '22, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a8584e178b3c216a8d75fc32ac58a095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muran123&#39;s gravatar image" />
<p><span>Muran123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muran123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '22, 10:01</strong> </span></p>
</div>
</div>
<div id="comments-container-85308" class="comments-container">
&#10;</div>
<div id="comment-tools-85308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85308-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

