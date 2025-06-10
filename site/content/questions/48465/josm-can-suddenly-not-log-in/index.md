+++
type = "question"
title = "JOSM can suddenly not log in"
description = '''I have been using JOSM for some months. Today I wanted to upload my latest edits, but got an OAuth dialog that requested me to enter my (prefilled) credentials. Pressing the &quot;Authorize now&quot; button gives me the error message saying: &quot;The automatic process for retrieving an OAuth Access Token from the...'''
date = "2016-03-02T19:01:00Z"
lastmod = "2016-03-05T09:37:00Z"
weight = 48465
keywords = [ "oauth", "josm" ]
aliases = [ "/questions/48465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM can suddenly not log in](/questions/48465/josm-can-suddenly-not-log-in)

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
<span id="post-48465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48465-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been using JOSM for some months. Today I wanted to upload my latest edits, but got an OAuth dialog that requested me to enter my (prefilled) credentials. Pressing the "Authorize now" button gives me the error message saying: "The automatic process for retrieving an OAuth Access Token from the OSM server failed. Please try again or choose another kind of authorization process, i.e. semi-automatic or manual autorization."</p>
<p>Then I select the semi-automatic process and press Receive Request Token. A status box appears for a short while and then nothing happens.</p>
<p>When I select the manual process, I don't know where to get the info needed. The dialog does not say and I cannot find anything in my OSM account that looks like it. Not even <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/OAuthAuthorisationWizard#Manualauthorisationprocess">https://josm.openstreetmap.de/wiki/Help/Dialog/OAuthAuthorisationWizard#Manualauthorisationprocess</a> gives a hint to where to get these.</p>
<p>JOSM is not registered under "My Authorised Applications" on openstreetmap.org. I have used it many times for several months without any issue.</p>
<p>I start JOSM via Java Web Start and have cleared the cache, even waited 5 hours, with no result.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '16, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/b65d3f18edb40b55ac321b01453a6b41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simonmikkelsen-dk&#39;s gravatar image" />
<p><span>simonmikkels...</span><br />
<span class="score" title="96 reputation points">96</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simonmikkelsen-dk has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-48465" class="comments-container">
<span id="48467"></span>
<div id="comment-48467" class="comment">
<div id="post-48467-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="/questions/48014/josm-enter-credentials-for-osm-api-failure">there</a>, recently, the user also was not successful in setting up OAuth. Hmm ...</p>
<p>I just used JOSM 9900 on openjdk version 1.8.0_74 (64 bit) on Linux to upload changes with an OAuth (which I have set up since a long time) and no Webstart.</p>
<p>Some more info may be useful: Did you use OAuth before (in the "some months") or the plain username+password login for JOSM? Which version of JOSM do you use now? Which Java version? Maybe you just should open a new ticket with your version information (use the JOSM bug report function in JOSM's help menu) - please leave a not here if you do so.</p>
<p>"Register your application" on the "My Authorised Applications" page in your openstreetmap.org user settings should be the thing which you need for the manual process, but I currently cannot help you any more with that.</p>
</div>
<div id="comment-48467-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 19:08)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48468"></span>
<div id="comment-48468" class="comment">
<div id="post-48468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that very recently a new JOSM version was <a href="https://josm.openstreetmap.de/wiki/Changelog">released</a> (2016-02-28: Stable release r9900). The notes list "OAuth improvements" as a "minor enhancement". So maybe that broke something for you. I <em>guess</em> your experience could be related to <a href="https://josm.openstreetmap.de/ticket/7612">ticket/7612</a>. There <a href="https://josm.openstreetmap.de/query?status=assigned&amp;status=closed&amp;status=needinfo&amp;status=new&amp;status=reopened&amp;keywords=~oauth&amp;desc=1&amp;order=id">are some recently created</a> tickets about oauth in JOSM. ... maybe <a href="https://josm.openstreetmap.de/ticket/12584">ticket/12584</a> is the same problem you have.</p>
</div>
<div id="comment-48468-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 19:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48465-form-container" class="comment-form-container">
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

<span id="48498"></span>

<div id="answer-container-48498" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48498-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of the bugs referred mentioned a Java upgrade had fixed it. I upgraded to Oracle Java build 1.8.0_74-b02 (64 bit) on my Linux box but it did not fix the issues when I used Java Webstart.</p>
<p>When I downloaded the jar-file and ran it from the command line, it worked. This is good enough for me - as a Java developer I have never been a fan of Java Webstart anyway :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '16, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/b65d3f18edb40b55ac321b01453a6b41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simonmikkelsen-dk&#39;s gravatar image" />
<p><span>simonmikkels...</span><br />
<span class="score" title="96 reputation points">96</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simonmikkelsen-dk has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-48498" class="comments-container">
<span id="48499"></span>
<div id="comment-48499" class="comment">
<div id="post-48499-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I hope you don't mind - I've accepted this as an answer (since you won't be able to do it yourself, since it's your answer to your question).</p>
</div>
<div id="comment-48499-info" class="comment-info">
<span class="comment-age">(04 Mar '16, 11:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48506"></span>
<div id="comment-48506" class="comment">
<div id="post-48506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for accepting. I looked for the option but could not find it, so I assumed that rule existed.</p>
</div>
<div id="comment-48506-info" class="comment-info">
<span class="comment-age">(05 Mar '16, 08:11)</span> <span class="comment-user userinfo">simonmikkels...</span>
</div>
</div>
<span id="48507"></span>
<div id="comment-48507" class="comment">
<div id="post-48507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the solution! Just for reference: Could you mention which java version you had before? And did you try it without Webstart and that older version?</p>
</div>
<div id="comment-48507-info" class="comment-info">
<span class="comment-age">(05 Mar '16, 09:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48509"></span>
<div id="comment-48509" class="comment">
<div id="post-48509-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Prev version: java -version java version "1.7.0_80" Java(TM) SE Runtime Environment (build 1.7.0_80-b15) Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)</p>
<p>This version also works when not started with WebStart.</p>
</div>
<div id="comment-48509-info" class="comment-info">
<span class="comment-age">(05 Mar '16, 09:37)</span> <span class="comment-user userinfo">simonmikkels...</span>
</div>
</div>
</div>
<div id="comment-tools-48498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48498-form-container" class="comment-form-container">
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

