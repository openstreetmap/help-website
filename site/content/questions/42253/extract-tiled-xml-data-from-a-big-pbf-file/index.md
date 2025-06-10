+++
type = "question"
title = "Extract tiled xml data from a big pbf file"
description = '''I&#x27;d like to extract small xml files of tiled osm data from a pbf file. These xml files should contain data square map boxes. I&#x27;d like to have one xml file for each tile that is touched by the original pbf file. I used osmosis to extract one tile, which took 10 minutes for a pbf file of 2GB. This is ...'''
date = "2015-04-10T17:51:00Z"
lastmod = "2015-11-11T06:30:00Z"
weight = 42253
keywords = [ "osmconvert", "extract", "osmosis" ]
aliases = [ "/questions/42253" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Extract tiled xml data from a big pbf file](/questions/42253/extract-tiled-xml-data-from-a-big-pbf-file)

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
<span id="post-42253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42253-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to extract small xml files of tiled osm data from a pbf file. These xml files should contain data square map boxes. I'd like to have one xml file for each tile that is touched by the original pbf file. I used osmosis to extract one tile, which took 10 minutes for a pbf file of 2GB. This is probably due to the size of the pbf file (and IO speed), and not dependent on the size of my bounding box. Is there a tool that lets me extract lots of bounding boxes at once?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '15, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/edf8c89adb71d4763f9c75a6892f1388?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marian&#39;s gravatar image" />
<p><span>Marian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marian has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '15, 17:54</strong> </span></p>
</div>
</div>
<div id="comments-container-42253" class="comments-container">
&#10;</div>
<div id="comment-tools-42253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42253-form-container" class="comment-form-container">
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

<span id="42254"></span>

<div id="answer-container-42254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42254-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the <a href="https://github.com/MaZderMind/osm-history-splitter">OSM History Splitter</a> which processes history files as well as normal PBFs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42254" class="comments-container">
<span id="42257"></span>
<div id="comment-42257" class="comment">
<div id="post-42257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It doesn't compile on my ubuntu machine... (fails to find <code>boost/utility.hpp</code>)</p>
</div>
<div id="comment-42257-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 21:57)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
<span id="42309"></span>
<div id="comment-42309" class="comment">
<div id="post-42309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10818/marian">@Marian</a> Please install <code>libboost-dev</code>.</p>
</div>
<div id="comment-42309-info" class="comment-info">
<span class="comment-age">(13 Apr '15, 08:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42387"></span>
<div id="comment-42387" class="comment">
<div id="post-42387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I got it to run but it crashes if there are more than 30 bounding boxes in the config file.</p>
</div>
<div id="comment-42387-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 13:25)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
<span id="42431"></span>
<div id="comment-42431" class="comment">
<div id="post-42431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Turns out RAM usage grows quickly with the amount of bounding boxes so only a few bboxes can be extracted at a time.</p>
</div>
<div id="comment-42431-info" class="comment-info">
<span class="comment-age">(18 Apr '15, 12:41)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
<span id="42455"></span>
<div id="comment-42455" class="comment">
<div id="post-42455-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You might want to try the <code>--hardcut</code> option which uses less RAM. Else just run the program multiple times. The problem is (you say you want to produce &gt; 100.000 extracts) that a list of nodes and ways needs to be kept in memory for all these, and most programs will use an array-like structure for efficiency. It might be possible to switch osm-history-splitter to a list-like structure using small changes in the code.</p>
</div>
<div id="comment-42455-info" class="comment-info">
<span class="comment-age">(19 Apr '15, 18:46)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42254-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42255"></span>

<div id="answer-container-42255" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42255-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> ... it has several clipping features.</p>
<p>Read the instructions in wiki page carefully.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-42255" class="comments-container">
<span id="42256"></span>
<div id="comment-42256" class="comment">
<div id="post-42256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide an example of how to extract two bboxes from one pbf file using osmconvert?</p>
</div>
<div id="comment-42256-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 19:54)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
<span id="42261"></span>
<div id="comment-42261" class="comment">
<div id="post-42261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you try the clear example at</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Osmconvert#Clipping_based_on_Longitude_and_Latitude">http://wiki.openstreetmap.org/wiki/Osmconvert#Clipping_based_on_Longitude_and_Latitude</a></p>
<p>If you want two bboxes extracted, you should call this command twice with diferent parameters ... Success?</p>
</div>
<div id="comment-42261-info" class="comment-info">
<span class="comment-age">(11 Apr '15, 06:48)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="42302"></span>
<div id="comment-42302" class="comment">
<div id="post-42302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to do this more than 100k times. I was wondering if there is a more efficient way than parsing the entire pbf file each time.</p>
</div>
<div id="comment-42302-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 23:13)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
</div>
<div id="comment-tools-42255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42255-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42456"></span>

<div id="answer-container-42456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42456-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to create a huge number of extracts then perhaps installing a local Overpass database and extracting from there could be the fastest way. See <a href="http://overpass-api.de/no_frills.html">http://overpass-api.de/no_frills.html</a> for instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '15, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42456" class="comments-container">
<span id="46519"></span>
<div id="comment-46519" class="comment">
<div id="post-46519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why do you recommend creating a local overpass database over using an existing overpass service? Even in production, 10000 requests per day is way beyond what I need. Is the local db faster?</p>
</div>
<div id="comment-46519-info" class="comment-info">
<span class="comment-age">(10 Nov '15, 23:21)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
<span id="46521"></span>
<div id="comment-46521" class="comment">
<div id="post-46521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you're just doing this once for 5 or 10 bounding boxes then I guess it's ok. Else you come close to abusing the existing Overpass server - the local db may not be faster but it sure is fairer!</p>
</div>
<div id="comment-46521-info" class="comment-info">
<span class="comment-age">(11 Nov '15, 01:26)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46522"></span>
<div id="comment-46522" class="comment">
<div id="post-46522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The wiki page says 10.000 requests are ok. If 10 already is abuse, I'll sure set up my own. <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
</div>
<div id="comment-46522-info" class="comment-info">
<span class="comment-age">(11 Nov '15, 06:30)</span> <span class="comment-user userinfo">Marian</span>
</div>
</div>
</div>
<div id="comment-tools-42456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42456-form-container" class="comment-form-container">
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

