+++
type = "question"
title = "[closed] Dissector Tree Display Format"
description = '''Hi, Iam trying for custom dissector bit wise operation octet by octet.my payload may contain max of 255 octets. while display my tree i get the value as  [-] parent tree   [-] subtree   ..1. .... = id_present : TRUE (0x01)  ...0 11.. = length : TRUE (0x01)   { &amp;amp;hf_length,  { &quot;Length Present &quot;, &quot;...'''
date = "2014-06-03T02:00:00Z"
lastmod = "2014-06-03T02:12:00Z"
weight = 33335
keywords = [ "tree", "display", "format" ]
aliases = [ "/questions/33335" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Dissector Tree Display Format](/questions/33335/dissector-tree-display-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33335-score" class="post-score" title="current number of votes">0</div><span id="post-33335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Iam trying for custom dissector bit wise operation octet by octet.my payload may contain max of 255 octets.</p><p>while display my tree</p><p>i get the value as</p><pre><code>    [-] parent tree

            [-] subtree

                 ..1. .... = id_present : TRUE (0x01)
                 ...0 11.. = length     : TRUE (0x01)

        { &amp;hf_length,
           { &quot;Length Present   &quot;, &quot;Length_present.mine&quot;,FT_UINT8, BASE_HEX, VALS(length_vals), 0x40, NULL, HFILL }
        },</code></pre><p>i have 2 questions</p><p>How to Hide</p><pre><code>            ..1. .... =</code></pre><p>and only show</p><pre><code>            id_present : TRUE (0x01)</code></pre><p>I have tried use a value_string but its only taking 0x00 and 0x01. Anything wrong here? Is there any method doing it?</p><p>and next question is instead of</p><pre><code>               VALS(length_vals)</code></pre><p>can i use direct values that can be displayed? anyother method ?? my data is c9 that is 1100 10</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '14, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>03 Jun '14, 02:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33335" class="comments-container"><span id="33336"></span><div id="comment-33336" class="comment"><div id="post-33336-score" class="comment-score"></div><div class="comment-text"><p>Please don't raise a new question identical to one you raised earlier. If no-one has responded to your earlier question then it may not be clear what you are asking. Try to add clarifying comments if possible.</p></div><div id="comment-33336-info" class="comment-info"><span class="comment-age">(03 Jun '14, 02:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33335" class="comment-tools"></div><div class="clear"></div><div id="comment-33335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate of http://ask.wireshark.org/questions/33229/dissector-tree-hide-item" by grahamb 03 Jun '14, 02:11

</div>

</div>

</div>

