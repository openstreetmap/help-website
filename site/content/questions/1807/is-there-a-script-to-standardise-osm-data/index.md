+++
type = "question"
title = "Is there a script to standardise OSM data?"
description = '''Hi, I want to know if there is a script to standardise OSM data. Some examples:  address tags can be given to closed ways (with a building tag), nodes and ways with an addr:interpolation tag. The street can be given as an addr:street tag, as an associatedstreet relation, or just the closest street a...'''
date = "2010-12-14T13:50:00Z"
lastmod = "2010-12-16T13:58:00Z"
weight = 1807
keywords = [ "tool", "standardise", "data" ]
aliases = [ "/questions/1807" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a script to standardise OSM data?](/questions/1807/is-there-a-script-to-standardise-osm-data)

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
<span id="post-1807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to know if there is a script to standardise OSM data. Some examples:</p>
<ul>
<li>address tags can be given to closed ways (with a building tag), nodes and ways with an addr:interpolation tag. The street can be given as an addr:street tag, as an associatedstreet relation, or just the closest street availiable. Is there any tool to transform this into only nodes with an addr:housenumber, addr:street, addr:city ... tag?</li>
<li>Sometimes, when boundaries aren't availiable, <code>is_in</code> tags are used. Since we can't draw boundaries from is_in tags, can we put is_in tags on streets if we have the boundaries? Or if we don't have boundaries nor is_in tags, use the nominatim approach and choose the closest city/village.</li>
<li>...</li>
</ul>
<p>This would result in an OSM file that isn't suited for editing anymore, but can more easily be used by other tools.</p>
<p>This should be possible, since it's only a fraction of the work that nominatim does, but I wonder if there is also a separate tool or script to do it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tool" rel="tag" title="see questions tagged &#39;tool&#39;">tool</span> <span class="post-tag tag-link-standardise" rel="tag" title="see questions tagged &#39;standardise&#39;">standardise</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '10, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-1807" class="comments-container">
<span id="1819"></span>
<div id="comment-1819" class="comment">
<div id="post-1819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not entirely sure what you're asking in this question. When you say "OSM data"- what specific kind of data do you mean? Addresses? Something else?</p>
</div>
<div id="comment-1819-info" class="comment-info">
<span class="comment-age">(15 Dec '10, 12:15)</span> <span class="comment-user userinfo">emacsen</span>
</div>
</div>
<span id="1827"></span>
<div id="comment-1827" class="comment">
<div id="post-1827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well,</p>
<p>I would love to have a general script: where all data is kept, as long as it's documented and in one format.</p>
<p>But if you could give me an example that does the things I mentionned, I think I would be able to also adapt it to other generalisations.</p>
<p>what I would want the most is:</p>
<ul>
<li><p>apply a tag to all objects in a closed way or a closed relation</p></li>
<li><p>place a node on the centre of a closed way or relation with tags that come from that way/relation</p></li>
</ul>
<p>Off cource in script form, so that it can be automised.</p>
<p>Thanks</p>
</div>
<div id="comment-1827-info" class="comment-info">
<span class="comment-age">(15 Dec '10, 18:43)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-1807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1807-form-container" class="comment-form-container">
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

<span id="1838"></span>

<div id="answer-container-1838" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1838-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, there is no current tool available to do what you want. What you are looking for is a script that, for everything in the world that can be represented in OpenStreetMap in two or more different ways, pick one of the representations and convert all the others.</p>
<p>If you are just interested in sorting out tagging, then I would recommend the <a href="http://wiki.openstreetmap.org/wiki/Osmosis/TagTransform">TagTransform plugin for Osmosis</a>. I use this plugin daily in my rendering toolchain, for example to take the multiple different was of tagging a <a href="http://wiki.openstreetmap.org/wiki/Crossing">Zebra Crossing</a> and consolidate them into one tag. This makes the stylesheets easier to deal with.</p>
<p>More advanced geometry manipulation is done in a variety of tools, most noticeably during import by <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> / <a href="http://wiki.openstreetmap.org/wiki/Nominatim">nomintim</a>, but these are specific-purposed transformations into a specific data format rather than general-purpose routines that output openstreetmap data.</p>
<p>There is nothing stopping such a utility being created, it simply hasn't been done yet. The ultimate tool would let you pick between the representations depending on your needs - for example some people want <code>is_in</code> generated from polygons, but others prefer polygons generated from <code>is_in</code> tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '10, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-1838" class="comments-container">
<span id="1840"></span>
<div id="comment-1840" class="comment">
<div id="post-1840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The tagtransform plugin comes close. The only disadvantage is that it can't change between relations, ways and nodes. It can only edit the tags.</p>
<p>for osm2pgsql, I've read that it loses the info if two ways are connected. And I would not want to lose that data.</p>
<p>I agree on your vision about what the ultimate tool would be.</p>
</div>
<div id="comment-1840-info" class="comment-info">
<span class="comment-age">(16 Dec '10, 13:58)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-1838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1838-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1830"></span>

<div id="answer-container-1830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1830-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could probably do this sort of thing with PostGIS. You can use Osmosis or osm2pgsql to read from an .osm file, and output to a PostGreSQL database.</p>
<p>Then you can use PostGIS queries to find if an object is within a boundary polygon, or near a place, and add tags as appropriate. You can also collapse areas into points (e.g. make a POI out of a building or so).</p>
<p>Such queries could be scripted and automated if you want. Though I don't know of any ready made scripts to do the processing/standardisation that you describe. As you say, Nominatim does some of this processing, and its source code is available, which might be helpful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '10, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '10, 15:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-1830" class="comments-container">
&#10;</div>
<div id="comment-tools-1830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1830-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1829"></span>

<div id="answer-container-1829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm afraid I think the reason no one's answered this question is that, like me, they don't understand it.</p>
<p>I don't know what a script where all data is kept means. I thought you wanted address data, but now I'm just too confused, and I'm afraid others here are as well.</p>
<p>I'm going to take a stab at answering what I think your question is:</p>
<p>The first part seems to be "How can I programatically access OSM data?"</p>
<p>If so, the answer is several fold.</p>
<p>OSM is a database of geographic information and we provide several mechanisms of storing that data. The most popular consumable format of OSM data is the OSM XML file format. Usually when you see a .osm file, that file is in the OSM XML format, which is described in detail at <a href="http://wiki.openstreetmap.org/wiki/.osm"></a><a href="http://wiki.openstreetmap.org/wiki/.osm"></a><a href="http://wiki.openstreetmap.org/wiki/.osm">http://wiki.openstreetmap.org/wiki/.osm</a></p>
<p>The second part seems to be about programatically modifying OSM features to (using your terminology) "standardise them".</p>
<p>The short answer is that we don't provide a mechanism to do this, and you shouldn't consider modifying OSM data in an automated way without having a deep understanding of the data you're modifying (and often not even then).</p>
<p>Let's take your example of modifying addresses, using the is_in to add street or town data.</p>
<p>Speaking just about the US, I know this wouldn't work. There are places where the city/town you might think corresponds to an address doesn't. There's a long and complex story around this having to do with the names used for towns historically being the name of the post office and not the city, but the bottom line is you don't know.</p>
<p>Similarly, you might assume that a building in proximity to a street is addressed to that street, but you can't know that.</p>
<p>And if you make an assumption like that, modifying the data, then you make it more difficult to find the error and correct in the future.</p>
<p>Of course if you know the information for an area, you should modify it yourself, but this is not the same as carrying out an automated edit (ie running a bot). Bots are generally frowned upon because of their negative history with the project. More information on bots can be found here: <a href="http://wiki.openstreetmap.org/wiki/Bot"></a><a href="http://wiki.openstreetmap.org/wiki/Bot"></a><a href="http://wiki.openstreetmap.org/wiki/Bot">http://wiki.openstreetmap.org/wiki/Bot</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '10, 01:59</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-1829" class="comments-container">
<span id="1834"></span>
<div id="comment-1834" class="comment">
<div id="post-1834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The file shoudn't be used on OSM back again. It's just that, if there is less info availiable, the script guesses what it is and places it in the file. That way, a tool which uses the file doesn't have to guess again. But more important: if the data is availiable, it is sometimes as a node, a way or a relation. I would like to simplify it to nodes if possible.</p>
<p>I don't want te reupload the file, I know this would do bad things to the OSM database since the database is made for editing, not for usage by tools.</p>
</div>
<div id="comment-1834-info" class="comment-info">
<span class="comment-age">(16 Dec '10, 09:49)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-1829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1829-form-container" class="comment-form-container">
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

