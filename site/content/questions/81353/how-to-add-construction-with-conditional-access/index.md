+++
type = "question"
title = "How to add construction with conditional access?"
description = '''Hi everyone! There is a bridge in Parnu, which is close 7pm-5am Aug 16-30 due to construction works. What&#x27;s the common way of mapping this kind of information? Is there something like &quot;conditional construction&quot;? So far, I understand that the construction tag restricts access by default. How it would...'''
date = "2021-08-18T09:45:00Z"
lastmod = "2021-08-23T12:55:00Z"
weight = 81353
keywords = [ "access", "construction", "conditional", "routing" ]
aliases = [ "/questions/81353" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to add construction with conditional access?](/questions/81353/how-to-add-construction-with-conditional-access)

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
<span id="post-81353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81353-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>There is a bridge in Parnu, which is close 7pm-5am Aug 16-30 due to construction works. What's the common way of mapping this kind of information? Is there something like "conditional construction"? So far, I understand that the construction tag restricts access by default. How it would work if we add conditional access and construction tags in parallel. How OSRM routing will treat it?</p>
<p>Source: <a href="https://parnu.ee/uudised/muudatused-liikluskorralduses/4357-8-juunil-algab-paernu-kesklinna-silla-remont">https://parnu.ee/uudised/muudatused-liikluskorralduses/4357-8-juunil-algab-paernu-kesklinna-silla-remont</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '21, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d33327130c667fe7aeb4e207f01eb1b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bolt001&#39;s gravatar image" />
<p><span>Bolt001</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bolt001 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81353" class="comments-container">
&#10;</div>
<div id="comment-tools-81353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81353-form-container" class="comment-form-container">
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

<span id="81359"></span>

<div id="answer-container-81359" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81359-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bolt001 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Short term works is not represented. The situation should last eg at least several months to be considered for inclusion.</li>
<li><code>*:conditional=</code> is a regular, recurring restriction. Not one-off. It makes things messy to mix non-permanent events in it.</li>
<li>I doubt if any routers support <code>temporary:construction=* @ (2021 Aug 16-30 19:00-05:00)</code> <code>temporary:access=no @ (2021 Aug 16-30 19:00-05:00)</code> yet.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '21, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '21, 00:36</strong> </span></p>
</div>
</div>
<div id="comments-container-81359" class="comments-container">
<span id="81383"></span>
<div id="comment-81383" class="comment">
<div id="post-81383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, basically there's no way to map such restrictions? there's another case as well, where the crossing is restricted only for cars until 31.10.2021 6pm-6am: <a href="https://www.tsk-praha.cz/wps/portal/root/o-spolecnosti/mapa-staveb?poi=606454ffd8d9a78a0e9cee3d.">https://www.tsk-praha.cz/wps/portal/root/o-spolecnosti/mapa-staveb?poi=606454ffd8d9a78a0e9cee3d.</a></p>
</div>
<div id="comment-81383-info" class="comment-info">
<span class="comment-age">(20 Aug '21, 08:52)</span> <span class="comment-user userinfo">Bolt001</span>
</div>
</div>
<span id="81385"></span>
<div id="comment-81385" class="comment">
<div id="post-81385-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is possible to map such cases with <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a>. The point is that we do not want to map such short term restrictions which lie within regular update circles of data consumers like routing apps.</p>
</div>
<div id="comment-81385-info" class="comment-info">
<span class="comment-age">(20 Aug '21, 09:15)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81401"></span>
<div id="comment-81401" class="comment">
<div id="post-81401-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/19612/bolt001"></a><a href="https://help.openstreetmap.org/users/19612/bolt001">@Bolt001</a><br />
1. It's not "no way" to OSM. The cause is applications using OSM data usually don't update their data very frequently (even if they are not reviewed and directly used), so better keep these limited-time changes separate to avoid unintended problems. You would want to ask for the software you are using to support <code>temporary:*=</code>.<br />
2. This one you can add <code>motor_vehicle:conditional=no @ (18:00-06:00)</code>, but you must remember to change it back. (Which is another factor not favoring maintenance of shorter period data)<br />
3. Although <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions#Use_with_keys">https://wiki.openstreetmap.org/wiki/Conditional_restrictions#Use_with_keys</a> has a <code>motor_vehicle:conditional=no @ (2018 May 22-2018 Oct 7)</code> example, this is argued against in <a href="https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/temporary_(conditional)#Why_not_:conditional?">https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/temporary_(conditional)#Why_not_:conditional?</a> .</p>
</div>
<div id="comment-81401-info" class="comment-info">
<span class="comment-age">(21 Aug '21, 08:06)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="81420"></span>
<div id="comment-81420" class="comment">
<div id="post-81420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you a lot: <a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> and <a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a></p>
</div>
<div id="comment-81420-info" class="comment-info">
<span class="comment-age">(23 Aug '21, 12:55)</span> <span class="comment-user userinfo">Bolt001</span>
</div>
</div>
</div>
<div id="comment-tools-81359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81359-form-container" class="comment-form-container">
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

