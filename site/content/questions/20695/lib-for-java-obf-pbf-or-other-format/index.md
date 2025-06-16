+++
type = "question"
title = "Lib for Java OBF PBF or other format"
description = '''Hello I&#x27;m trying to write a small android application that must be used offline. Basically i need to find a lib to access osm data offline. I&#x27;ve read about PBF and OBF, and think they should be appropriate. But i&#x27;m having a hard time finding a lib. I don&#x27;t want to display the map or anything, i&#x27;d li...'''
date = "2013-03-13T16:01:00Z"
lastmod = "2013-03-14T16:16:00Z"
weight = 20695
keywords = [ "obf", "android", "pbf", "java", "library" ]
aliases = [ "/questions/20695" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Lib for Java OBF PBF or other format](/questions/20695/lib-for-java-obf-pbf-or-other-format)

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
<span id="post-20695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20695-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I'm trying to write a small android application that must be used offline.</p>
<p>Basically i need to find a lib to access osm data offline. I've read about PBF and OBF, and think they should be appropriate. But i'm having a hard time finding a lib.</p>
<p>I don't want to display the map or anything, i'd like to access raw data ... nodes, ways, relations ...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-obf" rel="tag" title="see questions tagged &#39;obf&#39;">obf</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '13, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/b9f0f4cbcf36434849d09abe27afc90a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZARk&#39;s gravatar image" />
<p><span>ZARk</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZARk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '13, 07:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span></p>
</div>
</div>
<div id="comments-container-20695" class="comments-container">
&#10;</div>
<div id="comment-tools-20695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20695-form-container" class="comment-form-container">
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

<span id="20698"></span>

<div id="answer-container-20698" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20698-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong><a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a></strong> can read pbf as well as osm, osm.gz and osm.bz2. I've posted example code on the forum a while ago. It's not 100% up to date but should give you a first impression how you could use it:</p>
<p><a href="http://forum.openstreetmap.org/viewtopic.php?pid=213212#p213212">http://forum.openstreetmap.org/viewtopic.php?pid=213212#p213212</a></p>
<p>Additional features of Osmosis include filters and other pipeline elements to e.g. trim unwanted data while you are reading it. Osmosis is most commonly used as a stand-alone command line tool, but do not let that fool you: It is a decent choice as a Java library as well. I've used it in several of my projects.</p>
<p>However, I'm not an Android developer and do not know whether Osmosis works on Android. So take my recommendation with a grain of salt!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '13, 19:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-20698" class="comments-container">
<span id="20713"></span>
<div id="comment-20713" class="comment">
<div id="post-20713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Toranik !</p>
<p>Thanks for the link, i'm actually trying to build with your snippet i found when searching the forum.</p>
<p>But i'm actually having compilation issues when including the jar files from osmosis. So far it seems like the best solution (if I can compile on android with it)</p>
</div>
<div id="comment-20713-info" class="comment-info">
<span class="comment-age">(14 Mar '13, 16:16)</span> <span class="comment-user userinfo">ZARk</span>
</div>
</div>
</div>
<div id="comment-tools-20698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20698-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20696"></span>

<div id="answer-container-20696" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20696-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Pbf">OSM wiki page</a> has links to the protobuf code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '13, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '13, 17:37</strong> </span></p>
</div>
</div>
<div id="comments-container-20696" class="comments-container">
&#10;</div>
<div id="comment-tools-20696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20696-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20697"></span>

<div id="answer-container-20697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20697-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>via <a href="https://wiki.openstreetmap.org/wiki/O5m">wiki/O5m</a> I found recently <a href="https://github.com/kiselev-dv/o5m4j">o5m4j</a> ... a small java lib.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '13, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-20697" class="comments-container">
&#10;</div>
<div id="comment-tools-20697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20697-form-container" class="comment-form-container">
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

