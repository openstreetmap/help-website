+++
type = "question"
title = "how to highlight a street as user taps on it"
description = '''I am working on an application in android where I have to identify the streets where a parking slot is empty. So how can I highlight a street on OSM as the user taps on it? Thanks for your help'''
date = "2014-07-18T07:54:00Z"
lastmod = "2014-07-18T13:09:00Z"
weight = 34952
keywords = [ "android" ]
aliases = [ "/questions/34952" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to highlight a street as user taps on it](/questions/34952/how-to-highlight-a-street-as-user-taps-on-it)

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
<span id="post-34952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on an application in android where I have to identify the streets where a parking slot is empty. So how can I highlight a street on OSM as the user taps on it? Thanks for your help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '14, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1122d877473f3694e5355d5b8776eae8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shehzy&#39;s gravatar image" />
<p><span>shehzy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shehzy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34952" class="comments-container">
&#10;</div>
<div id="comment-tools-34952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34952-form-container" class="comment-form-container">
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

<span id="34956"></span>

<div id="answer-container-34956" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34956-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is too vague and is only about a user interface development. What you can ask on this help site is how a "street" is modelized in OSM : it's one or more <a href="http://wiki.openstreetmap.org/wiki/Way">ways (aka polylines)</a> carying a tag "<a href="http://wiki.openstreetmap.org/wiki/Key:highway">highway=*</a>" and possibly a <a href="http://wiki.openstreetmap.org/wiki/Street#Names_and_references">name and/or ref</a> tag. It's not necessarily geometrically continuous (one way attached to the next one) when it's interrupted by <a href="http://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout">roundabouts</a> which may have their own name and/or ref. The "highway" value may also change within the same street.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '14, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-34956" class="comments-container">
<span id="34963"></span>
<div id="comment-34963" class="comment">
<div id="post-34963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>actually I am absolutely new in OSM. I want to know is it possible to get the coordinates of a street as user taps on it in OSM?</p>
</div>
<div id="comment-34963-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 13:09)</span> <span class="comment-user userinfo">shehzy</span>
</div>
</div>
</div>
<div id="comment-tools-34956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34956-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34957"></span>

<div id="answer-container-34957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34957-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is essentially just lots and lots of data (see a previous answer to a different question <a href="http://help.openstreetmap.org/questions/32760/looking-for-a-description-of-how-the-map-is-shown-on-a-pc-rendering-process-but-no-technical-details/33010">here</a>). It's entirely up to you how what technologies you use to represent that data and to allow the user to interact with it.<br />
</p>
<p>Without knowing how you're doing that (Displaying information over pre-rendered tiles? Displaying vectors?) or even what technology you're using for Android development (Android Java? Xamarin? Cordova?) it's possible to do little more than point you at the <a href="http://wiki.openstreetmap.org/wiki/Category:Android">Android category in the wiki</a> and at previous "what is OSM" answers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '14, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-34957" class="comments-container">
&#10;</div>
<div id="comment-tools-34957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34957-form-container" class="comment-form-container">
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

