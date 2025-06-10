+++
type = "question"
title = "osm2pgsql dosnt work with planet-latest.osm.bz2 getting error"
description = '''While configuring osm2pgsql (OSM MAP) on ubuntu 9.10 all is done but when i am going to extract Planet in to database get some error. Executing command :  ./osm2pgsql -S default.style --slim -d gis2 -C 1024 --number-processes=1 --cache-strategy=dense /home/baban/Mapserver/planet-latest.osm.bz2  I GE...'''
date = "2011-11-21T06:40:00Z"
lastmod = "2011-12-12T06:40:00Z"
weight = 9142
keywords = [ "planet", "error" ]
aliases = [ "/questions/9142" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql dosnt work with planet-latest.osm.bz2 getting error](/questions/9142/osm2pgsql-dosnt-work-with-planet-latestosmbz2-getting-error)

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
<span id="post-9142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9142-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While configuring osm2pgsql (OSM MAP) on ubuntu 9.10 all is done but when i am going to extract Planet in to database get some error. Executing command :</p>
<pre><code> ./osm2pgsql -S default.style --slim -d gis2 -C 1024 --number-processes=1 --cache-strategy=dense /home/baban/Mapserver/planet-latest.osm.bz2</code></pre>
<p>I GET ERROR AS :</p>
<pre><code>Unknown node type 8
Processing: Node(109850k 36.9k/s) Way(0k 0.00k/s) Relation(0 0.00/s)WARNING: Found Out of order node 142301185 (33693398,1) - this will impact the cache efficiency
Processing: Node(119970k 36.4k/s) Way(0k 0.00k/s) Relation(0 0.00/s)Entity: line 194701204: parser error : AttValue: &#39; expected
 &lt;node id=&quot;153093405&quot; lat=&quot;29.9738900&quot; lon=&quot;-95.4713280&quot; timestamp=&quot;2010-01-07T2
                                                                               ^
Entity: line 194701204: parser error : attributes construct error
 &lt;node id=&quot;153093405&quot; lat=&quot;29.9738900&quot; lon=&quot;-95.4713280&quot; timestamp=&quot;2010-01-07T2
                                                                               ^
Entity: line 194701204: parser error : Couldn&#39;t find end of Start Tag node
 &lt;node id=&quot;153093405&quot; lat=&quot;29.9738900&quot; lon=&quot;-95.4713280&quot; timestamp=&quot;2010-01-07T2
                                                                               ^
../../planet-latest.osm.bz2 : failed to parse
Error occurred, cleaning up</code></pre>
<p>Can anybody help to resolve this problem so that i can configure OSM successfully. I have 1 GB RAM on my system</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '11, 06:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6415fd7bc63406c5ab1bc64cc29bb52a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baban&#39;s gravatar image" />
<p><span>baban</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baban has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '11, 16:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-9142" class="comments-container">
&#10;</div>
<div id="comment-tools-9142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9142-form-container" class="comment-form-container">
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

<span id="9214"></span>

<div id="answer-container-9214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9214-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To me this error suggests that your input XML file is damaged part way through, probably truncated.</p>
<p>Check that you downloaded the full planet file. It should be about 18Gb. You could also run a command : <code>md5sum planet-latest.osm.bz2</code> ....and check the resulting number matches with the md5 checksum shown on <a href="http://planet.openstreetmap.org"></a><a href="http://planet.openstreetmap.org">http://planet.openstreetmap.org</a> (check that the file is exactly the same)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '11, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-9214" class="comments-container">
<span id="9446"></span>
<div id="comment-9446" class="comment">
<div id="post-9446-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Harry Sir,<br />
I checked md5 it shows differences then, I download some other planet.osm.bz2 file with checking md5 and it works !!! now I am generate_tiles</p>
</div>
<div id="comment-9446-info" class="comment-info">
<span class="comment-age">(12 Dec '11, 06:40)</span> <span class="comment-user userinfo">baban</span>
</div>
</div>
</div>
<div id="comment-tools-9214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9254"></span>

<div id="answer-container-9254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9254-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-9254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Can you unzip the file and just try the same command with the .osm file ? I presume you've done that. If not, it's a formatting issue. Depending on the size of the file, open the file in a browser and check for formats. Hope this helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '11, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/db4cbce4d254722e59037ede98ca51fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deepGem&#39;s gravatar image" />
<p><span>deepGem</span><br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deepGem has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-9254" class="comments-container">
&#10;</div>
<div id="comment-tools-9254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9254-form-container" class="comment-form-container">
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

