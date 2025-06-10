+++
type = "question"
title = "Embed idEditor into another website"
description = '''Hello,  I&#x27;m in the process of making a website that enables users to add street names to an OSM map.  The website will have only one functionality, which is adding street names for unnamed streets.  I want to create this website for my hometown, because streets in my hometown are not named. So, I wa...'''
date = "2018-02-28T17:30:00Z"
lastmod = "2018-02-28T17:52:00Z"
weight = 62486
keywords = [ "ideditor", "development" ]
aliases = [ "/questions/62486" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Embed idEditor into another website](/questions/62486/embed-ideditor-into-another-website)

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
<span id="post-62486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm in the process of making a website that enables users to add street names to an OSM map.</p>
<p>The website will have only one functionality, which is adding street names for unnamed streets.</p>
<p>I want to create this website for my hometown, because streets in my hometown are not named. So, I want to provide an easy way for the locals in my community to suggest and add street names for unnamed streets.</p>
<p>I've used idEditor and I like the feature where I can click on a street and it will give me the option of changing a street name, or add one if none already exists.</p>
<p>I want to use this UI in my future website, so that the website basically has a map, the user comes and chooses a street (like in idEditor) and the user will be prompted to enter a street name.</p>
<p>Pretty simple I guess, but my experience in web development is pretty minimal and I don't really know where to start from.</p>
<p>I would appreciate any guidance or help.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '18, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/84512dd471510fabe0c283cea3f9a415?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aljulanda&#39;s gravatar image" />
<p><span>aljulanda</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aljulanda has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '18, 22:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62486" class="comments-container">
&#10;</div>
<div id="comment-tools-62486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62486-form-container" class="comment-form-container">
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

<span id="62487"></span>

<div id="answer-container-62487" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62487-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Pretty simple I guess, but my experience in web development is pretty minimal and I don't really know where to start from. I would appreciate any guidance or help.</p>
</blockquote>
<p>What you are describing does sound pretty simple! I'd advise you to fork a local copy of iD and get that working first.</p>
<p>Once you are comfortable with the basics of using git, building a JavaScript project, and deploying the app somewhere for testing, then you can change it so that it only uses the presets/fields that you are interested in.</p>
<p>To replace the presets, you can just set <code>iD.data.presets =</code> to something else, and call <code>init()</code> to replace them.</p>
<p>Here is an example app I made for "building damage assessment". The only file that is changed from default iD is the <code>index.html</code>. In it, I did this:</p>
<ul>
<li>replaced all the presets, adding only a few presets and fields for tagging building damage</li>
<li>added some CSS so things would render a bit different</li>
<li>adjusted the limits on the feature filters (In this case, to show all the buildings, but you could also use this trick to turn off everything except roads).</li>
</ul>
<p><a href="https://github.com/bhousel/iD/blob/ace02741ed8cab1cb68103696a4a55710b6a95db/index.html">https://github.com/bhousel/iD/blob/ace02741ed8cab1cb68103696a4a55710b6a95db/index.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '18, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '18, 17:53</strong> </span></p>
</div>
</div>
<div id="comments-container-62487" class="comments-container">
&#10;</div>
<div id="comment-tools-62487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62487-form-container" class="comment-form-container">
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

