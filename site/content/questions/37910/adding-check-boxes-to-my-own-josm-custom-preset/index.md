+++
type = "question"
title = "adding check boxes to my own JOSM custom preset"
description = '''I am working on a preset to apply to fuel stations. I want to use check boxes to enter data values for certain keys, for example,  &amp;lt;check key=&quot;fuel:gasoline_95&quot; text=&quot;Gas 95&quot; default=&quot;off&quot; delete_if_empty=&quot;true&quot; /&amp;gt;  What I would like is for the tag value to be set to &quot;no&quot; if the check box is u...'''
date = "2014-10-24T03:10:00Z"
lastmod = "2014-10-26T08:22:00Z"
weight = 37910
keywords = [ "josm", "preset", "check_box" ]
aliases = [ "/questions/37910" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [adding check boxes to my own JOSM custom preset](/questions/37910/adding-check-boxes-to-my-own-josm-custom-preset)

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
<span id="post-37910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37910-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-37910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a preset to apply to fuel stations. I want to use check boxes to enter data values for certain keys, for example,</p>
<pre><code>&lt;check key=&quot;fuel:gasoline_95&quot; text=&quot;Gas 95&quot; default=&quot;off&quot; delete_if_empty=&quot;true&quot;  /&gt;</code></pre>
<p>What I would like is for the tag value to be set to "no" if the check box is unchecked and "yes" if the check box is checked. I tried removing the delete_if_empty="true" phrase but it had no effect at all. Neither did changing "true" to "false". The only behavior I observe is that the key doesn't appear if the box is left unchecked.</p>
<p>Is there a way to do this? Thanks....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-preset" rel="tag" title="see questions tagged &#39;preset&#39;">preset</span> <span class="post-tag tag-link-check_box" rel="tag" title="see questions tagged &#39;check_box&#39;">check_box</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '14, 03:10</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '14, 13:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37910" class="comments-container">
&#10;</div>
<div id="comment-tools-37910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37910-form-container" class="comment-form-container">
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

<span id="37960"></span>

<div id="answer-container-37960" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37960-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to change it as follows :</p>
<pre><code>&lt;check key=&quot;fuel:gasoline_95&quot; text=&quot;Gas 95&quot; default=&quot;off&quot; value_on=&quot;yes&quot; value_off=&quot;no&quot;/&gt;</code></pre>
<p>The problem might be that you are not using the value_on and value_off. You can see the supported directives in the default preset file that comes along with JOSM. The default preset xml file is available at : <a href="http://josm.openstreetmap.de/svn/trunk/data/defaultpresets.xml">http://josm.openstreetmap.de/svn/trunk/data/defaultpresets.xml</a> Alternatively you can extract the defaultpresets.xml from the data folder in the JOSM JAR file.</p>
<p>I have written a Linux shell script to create the JOSM presets from text files a while back. You can find it here : <a href="https://github.com/primejyothi/JOSMPresetBuilder">https://github.com/primejyothi/JOSMPresetBuilder</a></p>
<p>Hope this helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '14, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/94b5bf3dcc698b1a4051d49f3204996e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="primej&#39;s gravatar image" />
<p><span>primej</span><br />
<span class="score" title="106 reputation points">106</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="primej has 2 accepted answers">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '14, 06:48</strong> </span></p>
</div>
</div>
<div id="comments-container-37960" class="comments-container">
<span id="37961"></span>
<div id="comment-37961" class="comment">
<div id="post-37961-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, that works almost perfectly. I say that because in testing my new preset, I learned that there are not two states for a checkbox but three. Checked, unchecked and, for lack of a better term, cleared. When the preset is first called all boxes are a light blue color. If I clear the checkbox by clicking on it until the blue color changes to white, the resultant tag will be set to "no". If I tick it, the tag will be "yes", as expected. If I do nothing, that is I do not tick it and I do not clear it, the tag does not get applied to the selection at all.</p>
</div>
<div id="comment-37961-info" class="comment-info">
<span class="comment-age">(26 Oct '14, 07:37)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="37962"></span>
<div id="comment-37962" class="comment">
<div id="post-37962-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To continue:</p>
<p>Cycling through the clicks on a first call of the preset, the first click turns the check mark on and sets the tag to "yes", the next click clears the check mark and sets the tag to "no, the next resets the blue color to the box and causes the tag to not appear at all.</p>
<p>At any rate, thanks for the great answer. I have adjusted my presets and they are working MUCH better than before. I have your preset builder already but haven't fooled with it enough to know if it will help me or hinder me as yet &lt;g&gt;</p>
</div>
<div id="comment-37962-info" class="comment-info">
<span class="comment-age">(26 Oct '14, 07:38)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="37963"></span>
<div id="comment-37963" class="comment">
<div id="post-37963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a>, you are welcome, glad that I could help you. Your comments made me curious and looked through the defaultpresets.xml and found that the option disable_off for check box controls whether the tag to be present or not. If you set disable_off to true, the tag will not show up when it is unset. Setting it to true will cause to go through the cycles you mentioned in your first comment.</p>
</div>
<div id="comment-37963-info" class="comment-info">
<span class="comment-age">(26 Oct '14, 07:58)</span> <span class="comment-user userinfo">primej</span>
</div>
</div>
<span id="37964"></span>
<div id="comment-37964" class="comment">
<div id="post-37964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, it seems that adding disable_off to the control prevents setting the tag to "no". You can either set it to "yes" or if you leave it unset, the tag doesn't get applied. Unless I'm not understanding you perfectly.</p>
<p>I like the ability to have a tag set to "no", e.g. , when there is no diesel fuel at a particular station. Before I could either set fuel:diesel to "yes" or say nothing about diesel at all. Thanks to your original answer, I can have it three ways.</p>
<p>Please strike the word "almost" from my first comment above. &lt;g&gt;</p>
</div>
<div id="comment-37964-info" class="comment-info">
<span class="comment-age">(26 Oct '14, 08:22)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37960-form-container" class="comment-form-container">
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

