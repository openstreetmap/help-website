+++
type = "question"
title = "Creating a patch for a plugin"
description = '''I want to create a patch or any sort of tool that would allow for developers who use my plugin to apply the changes to the wireshark releases. I&#x27;ve looked at this document http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html Now that would be suffice, but it means the developers woul...'''
date = "2011-02-22T11:50:00Z"
lastmod = "2011-02-23T08:47:00Z"
weight = 2497
keywords = [ "patch", "plugin" ]
aliases = [ "/questions/2497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating a patch for a plugin](/questions/2497/creating-a-patch-for-a-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2497-score" class="post-score" title="current number of votes">1</div><span id="post-2497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to create a patch or any sort of tool that would allow for developers who use my plugin to apply the changes to the wireshark releases. I've looked at this document http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html</p><p>Now that would be suffice, but it means the developers would apply the patch, then compile wireshark with the made-changes. I don't want them to have to compile it.</p><p>So my question is, is there anyway to create a patch that they can apply to their install of wireshark?</p><p>Edit: just to clarify further: essentially what I want to implement is a situation where a developer who has wireshark already simply grabs the patch(whether it be an rpm or whatever) from a git repo and installs the plugin to their copy of wireshark through that...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-patch" rel="tag" title="see questions tagged &#39;patch&#39;">patch</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '11, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p><span>Rodayo</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '11, 11:27</strong> </span></p></div></div><div id="comments-container-2497" class="comments-container"></div><div id="comment-tools-2497" class="comment-tools"></div><div class="clear"></div><div id="comment-2497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2514"></span>

<div id="answer-container-2514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2514-score" class="post-score" title="current number of votes">0</div><span id="post-2514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The beauty of a plugin is that it is an self contained piece of code, so why not distribute that? But remember to also distribute the source code, as per GPL.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '11, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2514" class="comments-container"><span id="2522"></span><div id="comment-2522" class="comment"><div id="post-2522-score" class="comment-score"></div><div class="comment-text"><p>Right, but the user would still have to compile it...wouldn't they? As far as I know in order to include your plugin in the build some files needs to be modified as per README.plugins</p></div><div id="comment-2522-info" class="comment-info"><span class="comment-age">(23 Feb '11, 08:47)</span> <span class="comment-user userinfo">Rodayo</span></div></div></div><div id="comment-tools-2514" class="comment-tools"></div><div class="clear"></div><div id="comment-2514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

