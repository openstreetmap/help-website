+++
type = "question"
title = "Many questions, XML-definition,pbf or xml, extract parts from planet, coastlines, additional data beside osm-data"
description = '''Hi! I&#x27;m about to write my own renderer. But there are a few things I don&#x27;t find myself or that aren&#x27;t clear to me.  So I have a couple of questions, some easy, some maybe not.   1. I used on http://www.openstreetmap.org the &quot;Export&quot; link to get a file of &quot;OpenStreetMap-XML&quot;-Data of my area. The area...'''
date = "2012-10-23T15:43:00Z"
lastmod = "2012-10-24T14:22:00Z"
weight = 17130
keywords = [ "xml", "extraction", "pbf", "coastlines", "additional-data" ]
aliases = [ "/questions/17130" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Many questions, XML-definition,pbf or xml, extract parts from planet, coastlines, additional data beside osm-data](/questions/17130/many-questions-xml-definitionpbf-or-xml-extract-parts-from-planet-coastlines-additional-data-beside-osm-data)

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
<span id="post-17130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17130-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-17130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>Hi!
I&#39;m about to write my own renderer.
But there are a few things I don&#39;t find myself or that aren&#39;t clear to me.
&#10;So I have a couple of questions, some easy, some maybe not.
&#10; 1. I used on http://www.openstreetmap.org the &quot;Export&quot; link to get a file of &quot;OpenStreetMap-XML&quot;-Data of my area. The area was around 1km x 1km.
Where do I find the official definition for this XML? Which tag-names do exist?
?xml - osm, bounds, node, tag, nd
(In my following questions I might refer to them as tag-objects.)
&#10; 2. For example there were these nd ref=&quot;[somenumber]&quot; -tags, all contained in some way-objects.
So I just assume the number in the ref-attribute should reference some other tag-object in this xml-file. But it&#39;s not like that.
The numbers are either unique or sometimes happen to be in another nd-object used there as ref also.
Is that a bug in the export function? Or a feature? :P 
&#10; 3. For general purposes of course I want to extract those datas related to a selected area myself out of the planet-file.
Assuming I use a xml-planet file: Do I have to look for all node-objects (A) with latitude and longitude inside my area, and then in a second run I would have to look for all tags which contain directly or indirectly aforementionened &quot;ref&quot;-attributes that point to those nodeobjects (A)? Do I have to do it a couple of times, in case there are &quot;ref&quot;-attributes pointing to another way-object?
&#10; 4. Though I would much prefer to work with a planet file in xml-format, I would switch to pbf-format, if it is much faster in the processing *and* if pbf is definitly state of art in the OSM-project.
Are the current planet files xml, or already pbf? Or is the pbf idea already outdated again?
Assuming I have a planet file in xml and one in pbf, will they both hold the same data, will one hold a subgroup of the other, or may both contain data that isn&#39;t in the other? - Or in short: What should be taken as the official planet file?
Assume I have to download the pbf file to get the &quot;official&quot; planet data: Which program to use to convert it all into an xml file?
&#10; 5. About coastline files: Seeing there are coastline files, does that mean that the coastlines are not included as tag-objects in the planet file, or are they only implicitly included, or are the coastline files just some sort of handy service for map-makers?
If they are only implicitly included: Is it difficult to generate those coastlines, so that I just should use the coastline files provided here, or is it fairly simply (technically and in CPU-usage) to generate the coastlines myself?
&#10; 6. Is it advisable to use the data from http://www.naturalearthdata.com? As far as I have read through the wiki-pages, mapnik uses them, and mapnik is used by openstreetmap.org themselves.
Do I need or is it advisable to use http://www.mapability.com/info/vmap1_index.html ? Are there any advantages using that?
&#10; 7. Last but not least: Should I better use the OSM forums (http://forum.openstreetmap.org/index.php - no link on the homepage) or the help-section (https://help.openstreetmap.org - prominent link on the homepage) for questions? If it&#39;s ok I would prefer this help-section. :) In the future I will probably try the forum, to avoid the automatic styles being applied here. 
&#10;I&#39;m sure I won&#39;t run out of questions. :P
&#10;Greetings
WS</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-coastlines" rel="tag" title="see questions tagged &#39;coastlines&#39;">coastlines</span> <span class="post-tag tag-link-additional-data" rel="tag" title="see questions tagged &#39;additional-data&#39;">additional-data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '12, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1d3aa062ab2624577c100844c482d071?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WhyStand2&#39;s gravatar image" />
<p><span>WhyStand2</span><br />
<span class="score" title="8 reputation points">8</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WhyStand2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17130" class="comments-container">
<span id="17132"></span>
<div id="comment-17132" class="comment">
<div id="post-17132-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>What you should definitely do is to ask one question at a time - nobody is going to write an answer that covers all these questions.</p>
</div>
<div id="comment-17132-info" class="comment-info">
<span class="comment-age">(23 Oct '12, 16:05)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
<span id="17135"></span>
<div id="comment-17135" class="comment">
<div id="post-17135-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried, but it took from before you added your comment ;)</p>
</div>
<div id="comment-17135-info" class="comment-info">
<span class="comment-age">(23 Oct '12, 16:26)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17130-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="17134"></span>

<div id="answer-container-17134" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17134-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many of the answers I think are on the wiki.</p>
<ol>
<li>Does <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OSM XML</a> cover things?</li>
<li>The <code>&lt;nd ref="292403538"/&gt;</code> lines should be part of a &lt;way&gt; definition. A way is a sorted list of nodes, and the way can (probably will) have tags with key (k) and value (v). Nearer the start of the file you should find a &lt;node&gt; definition for the node with the relevant reference id, which will also have lat and lon values, version details, and may have tags with k/v properties as well.</li>
<li>You might find there is an <a href="https://wiki.openstreetmap.org/wiki/Extract">extract</a> for your area of interest already available. If not look at <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> which can cut an area from a larger extract.</li>
<li>If they are generated at the same time they should hold the same information. I understand working with PBF for many uses is faster, but I think usually when rendering the data is imported into a spatial database rather than being processed directly from the OSM data (whether XML or PBF).</li>
<li>I think the Coastline files are something Mapnik uses to speed things up. See the bit about the <a href="https://wiki.openstreetmap.org/wiki/Coastline_error_checker">coastline error checker</a>. Ah, and the bit about Rendering on <a href="https://wiki.openstreetmap.org/w/index.php?title=Coastline&amp;oldid=773274">this old edit</a> of the coastline page.</li>
<li>I think VMAP1 is for vertical elevations. If so then the OSM Mapnik doesn't use it, but if you are writing your own then you might want to use it, or maybe <a href="https://wiki.openstreetmap.org/wiki/SRTM">SRTM</a>. The cyclemap includes contours and hill shading for example and this isn't from the OSM dataset.</li>
<li>Tricky. You might want to also look at the <a href="http://lists.openstreetmap.org/listinfo">mailing lists</a> and <a href="http://irc.openstreetmap.org/">irc channels</a>. My preferences are for email and irc, but also watch the help.osm.org rss feed. The forums as well take up too much of my time so I visit those rarely. Other people are active there though.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '12, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17134" class="comments-container">
<span id="17137"></span>
<div id="comment-17137" class="comment">
<div id="post-17137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! And thank you for the answer. I will ask the remaining questions again in single threads. Might be better. =) 1. I found that, and now I found the links to the definitions on that page, too. 2. That's how I imagined it should be. The exported file from the openstreetmap.org export function wasn't like that. ): 3. I hope the definitions will enable me to write my own extractor. 4. True. 5. I will read through. 6. Ok. 7. =) I'll give this here a second try. Greetings WS</p>
</div>
<div id="comment-17137-info" class="comment-info">
<span class="comment-age">(23 Oct '12, 17:05)</span> <span class="comment-user userinfo">WhyStand2</span>
</div>
</div>
</div>
<div id="comment-tools-17134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17134-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17143"></span>

<div id="answer-container-17143" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17143-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(a slightly tangential answer)</p>
<p>What I'd suggest first is have a go at mapping something local to you and adding it to OSM (using either Potlatch in "advanced" mode so that you can see the tags and node numbers, or JOSM). Then have a go with something that <a href="https://wiki.openstreetmap.org/wiki/Rendering">renders the data</a> (not necessarily a full rendering database). That way you'll get familiar with the way the data is connected, and answers to questions like "what's an 'nd' in a way definition" will reveal themselves.</p>
<p>On the last point, the questions that you're asking might fit here (though better one at a time!) or on the "dev" mailing list, or (with some context in a pastebin that you can refer to) one of the IRC channels. There is a "Development" area of the forum but it's relatively low traffic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '12, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17143" class="comments-container">
&#10;</div>
<div id="comment-tools-17143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17143-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17158"></span>

<div id="answer-container-17158" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17158-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>For me (loading the full planet) working with PBF files is faster not because of the file format "per se", but because they do not require to be uncompressed first (either to a separate, 330GB XML file or a memory buffer). It seems that the "official" format is now PBF, at least for older versions of the planet file.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '12, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-17158" class="comments-container">
&#10;</div>
<div id="comment-tools-17158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17158-form-container" class="comment-form-container">
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

