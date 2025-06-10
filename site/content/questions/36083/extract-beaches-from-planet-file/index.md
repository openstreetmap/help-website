+++
type = "question"
title = "Extract beaches from planet file"
description = '''Hi guys, I would like to show where a beach is. But I cant extract them. From the documentation they seem to be &quot;closed ways&quot; instead of nodes. I extract nodes succesfully with osmosis and this command line: osmosis --read-pbf file=planet-latest.osm.pbf --node-key-value keyValueList=&quot;amenity.restaur...'''
date = "2014-08-22T18:03:00Z"
lastmod = "2014-08-23T15:58:00Z"
weight = 36083
keywords = [ "ways", "extraction", "extract", "osmosis" ]
aliases = [ "/questions/36083" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract beaches from planet file](/questions/36083/extract-beaches-from-planet-file)

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
<span id="post-36083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I would like to show where a beach is. But I cant extract them. From the documentation they seem to be "closed ways" instead of nodes.</p>
<p>I extract nodes succesfully with osmosis and this command line:</p>
<pre><code>osmosis --read-pbf file=planet-latest.osm.pbf --node-key-value keyValueList=&quot;amenity.restaurant&quot; -- write-xml restaurant.xml</code></pre>
<p>When I want to extract ways (like beaches) I use this Osmosis command line:</p>
<pre><code>osmosis --read-pbf file=planet-latest.osm.pbf --way-key-value keyValueList=&quot;natural.beach&quot; --used-node --write-xml beaches.xml</code></pre>
<p>However this doesnt work. The process starts:</p>
<pre><code>Pipeline executing, waiting for completion.</code></pre>
<p>But after a while a get an error:</p>
<pre><code>java.util.zip.DataFormatException: incorrect data check</code></pre>
<p>I have downloaded 3 planet files to make sure the data isnt currupt but this happens all the time.</p>
<p>How do I extract these beaches?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '14, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcec43f8f6c9d5b869aa5bdc56eb673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NLanaconda&#39;s gravatar image" />
<p><span>NLanaconda</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NLanaconda has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '14, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-36083" class="comments-container">
<span id="36115"></span>
<div id="comment-36115" class="comment">
<div id="post-36115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Works fine here using the latest osmosis version (0.43.1). Did you compare the MD5 checksum of your download?</p>
</div>
<div id="comment-36115-info" class="comment-info">
<span class="comment-age">(23 Aug '14, 08:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36121"></span>
<div id="comment-36121" class="comment">
<div id="post-36121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Checked it with MD5 but the checksum is different, what does that mean? The download is corrupt?</p>
</div>
<div id="comment-36121-info" class="comment-info">
<span class="comment-age">(23 Aug '14, 11:45)</span> <span class="comment-user userinfo">NLanaconda</span>
</div>
</div>
<span id="36123"></span>
<div id="comment-36123" class="comment">
<div id="post-36123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, if the MD5 doesn't match, it's a corrupt download.</p>
</div>
<div id="comment-36123-info" class="comment-info">
<span class="comment-age">(23 Aug '14, 11:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36129"></span>
<div id="comment-36129" class="comment">
<div id="post-36129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, I've downloaded an osm.pbf (pbf is compressed?) file and it is 26.6 GB (<a href="ftp://ftp.spline.de/pub/openstreetmap/pbf/)">ftp://ftp.spline.de/pub/openstreetmap/pbf/)</a></p>
<p>Should I download a .osm.bz2 file instead of .pbf? Those are around 36G.</p>
</div>
<div id="comment-36129-info" class="comment-info">
<span class="comment-age">(23 Aug '14, 13:02)</span> <span class="comment-user userinfo">NLanaconda</span>
</div>
</div>
<span id="36130"></span>
<div id="comment-36130" class="comment">
<div id="post-36130-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just to be clear - if the MD5 for the file that you've downloaded doesn't match the value that it is supposed to be, then you have a corrupt download and you need to download it again. A corrupt download will cause the error that you are seeing (see <a href="https://help.openstreetmap.org/questions/14206/incorrect-data-check">https://help.openstreetmap.org/questions/14206/incorrect-data-check</a> ).</p>
</div>
<div id="comment-36130-info" class="comment-info">
<span class="comment-age">(23 Aug '14, 13:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36131"></span>
<div id="comment-36131" class="comment not_top_scorer">
<div id="post-36131-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thans SomeoneElse for pointing me the right direction. I'm downloading a new 26G file again :) Hopefully it will work out.</p>
</div>
<div id="comment-36131-info" class="comment-info">
<span class="comment-age">(23 Aug '14, 13:20)</span> <span class="comment-user userinfo">NLanaconda</span>
</div>
</div>
</div>
<div id="comment-tools-36083" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-36083-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="36135"></span>

<div id="answer-container-36135" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36135-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you strugle, I'd like to suggest another way to get your data: Overpass API: <a href="http://overpass-turbo.eu/s/4Hu">http://overpass-turbo.eu/s/4Hu</a></p>
<p>Because as other say, fetching 35GB and process it for hours just to extract a few thousand items (a few MB) doesn't make sense, esp. at the beginning :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '14, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-36135" class="comments-container">
&#10;</div>
<div id="comment-tools-36135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36135-form-container" class="comment-form-container">
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

