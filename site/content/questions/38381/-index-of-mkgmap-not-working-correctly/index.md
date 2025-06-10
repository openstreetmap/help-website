+++
type = "question"
title = "--index of Mkgmap not working correctly"
description = '''Hello, I am already desperate, because I am googling for weeks and could not find a working answer in any forum, so I ask on my own. By the way, I am quite new to Mkgmap and this forum. I want to create a map for my Garmin device based on OSM, which should allow searching for streets etc. At first I...'''
date = "2014-11-08T16:30:00Z"
lastmod = "2014-11-20T19:59:00Z"
weight = 38381
keywords = [ "mkgmap", "garmin", "index" ]
aliases = [ "/questions/38381" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [--index of Mkgmap not working correctly](/questions/38381/-index-of-mkgmap-not-working-correctly)

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
<span id="post-38381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38381-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am already desperate, because I am googling for weeks and could not find a working answer in any forum, so I ask on my own. By the way, I am quite new to Mkgmap and this forum.</p>
<p>I want to create a map for my Garmin device based on OSM, which should allow searching for streets etc. At first I downloaded a map from download.geofabrik.de (Sachsen-Anhalt in Germany). After that I was using Splitter, then Osmosis and Mkgmap to get preprocessed bounds, so at the end I could create a gmapsupp.img file with Mkgmap. The code is:</p>
<pre><code>java -jar ../Splitter/splitter.jar --output-dir=Sachsenanhaltkarte Sachsenanhaltkarte/sachsen-anhalt-latest.osm.pbf
&#10;osmosis \
    --read-pbf file=Sachsenanhaltkarte/sachsen-anhalt-latest.osm.pbf outPipe.0=data1 \
    --read-pbf file=Sachsenanhaltkarte/sachsen-anhalt-latest.osm.pbf outPipe.0=data2 \
    --tag-filter accept-relations boundary=administrative,postal_code inPipe.0=data1 outPipe.0=6 \
    --used-way inPipe.0=6 outPipe.0=7 \
    --tag-filter reject-relations inPipe.0=data2 outPipe.0=8 \
    --tag-filter accept-ways boundary=administrative,postal_code inPipe.0=8 outPipe.0=9 \
    --used-node inPipe.0=9 outPipe.0=10 \
    --used-node inPipe.0=7 outPipe.0=11 \
    --merge inPipe.0=10 inPipe.1=11 outPipe.0=12 \
    --write-pbf file=Sachsenanhaltkarte/mapboundaries.osm.pbf omitmetadata=true compress=deflate inPipe.0=12
&#10;java -cp ./mkgmap-r3316/mkgmap.jar \
    uk.me.parabola.mkgmap.reader.osm.boundary.BoundaryPreprocessor \
    Sachsenanhaltkarte/mapboundaries.osm.pbf \
    Sachsenanhaltkarte/bounds
&#10;java -jar mkgmap-r3316/mkgmap.jar \
    --output-dir=./Sachsenanhaltkarte \
    --route \
    --add-pois-to-areas \
    --bounds=./Sachsenanhaltkarte/bounds \
    --index \
    --gmapsupp \
    ./Sachsenanhaltkarte/6324*.osm.pbf</code></pre>
<p>All this code is from walkthroughs on the web. When I transfer the created gmapsupp.img-file to the Garmin-directory of my devices SD-card, I can use the map as I want. But when I search for streets, only some can be found (for example in "Dessau-Rosslau": only "Am Beckerbruch", no other road seems to exist in this town).</p>
<p>I have no idea what might be the problem. My OS is OpenSuse 13.1, the code is used in the bash shell, all programs are not older than 4 months (the time when I began to struggle with Mkgmap), java should be up-to-date, my device is a Garmin Oregon 600.</p>
<p>Can someone please help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '14, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/638743479d1c35705e5762371bb87113?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kardoffl&#39;s gravatar image" />
<p><span>Kardoffl</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kardoffl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38381" class="comments-container">
<span id="38690"></span>
<div id="comment-38690" class="comment">
<div id="post-38690-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still no solution... Seems like noone has ever encountered that problem, and noone knows how to solve it?</p>
</div>
<div id="comment-38690-info" class="comment-info">
<span class="comment-age">(20 Nov '14, 19:59)</span> <span class="comment-user userinfo">Kardoffl</span>
</div>
</div>
</div>
<div id="comment-tools-38381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38381-form-container" class="comment-form-container">
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

<span id="38404"></span>

<div id="answer-container-38404" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38404-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The boundaries in the Sachsenanhalt pbf are probably incomplete. You could make it yourself a lot easier by skipping the whole process of creating boundary data by downloading the complete world boundary set from mkgmap: <a href="http://www.mkgmap.org.uk/download/mkgmap.html">http://www.mkgmap.org.uk/download/mkgmap.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '14, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-38404" class="comments-container">
<span id="38411"></span>
<div id="comment-38411" class="comment">
<div id="post-38411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer. But I just tested it, the result did not change.</p>
<p>Could it be that I downloaded a buggy version of mkgmap? I already tried a map directly from the export function of OSM, and exactly the same streets appear while the others cannot be found.</p>
</div>
<div id="comment-38411-info" class="comment-info">
<span class="comment-age">(09 Nov '14, 19:22)</span> <span class="comment-user userinfo">Kardoffl</span>
</div>
</div>
</div>
<div id="comment-tools-38404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38404-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38383"></span>

<div id="answer-container-38383" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38383-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not familiar with the town, but when you try a ready made garmin suitable from one of the many <a href="http://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin/Download">providers</a> such as <a href="http://garmin.openstreetmap.nl">http://garmin.openstreetmap.nl</a> are more streets found.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '14, 23:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '14, 23:42</strong> </span></p>
</div>
</div>
<div id="comments-container-38383" class="comments-container">
<span id="38412"></span>
<div id="comment-38412" class="comment">
<div id="post-38412-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, with that page I will have working maps in the meantime while trying to compile my own maps.</p>
</div>
<div id="comment-38412-info" class="comment-info">
<span class="comment-age">(09 Nov '14, 19:26)</span> <span class="comment-user userinfo">Kardoffl</span>
</div>
</div>
</div>
<div id="comment-tools-38383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38383-form-container" class="comment-form-container">
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

