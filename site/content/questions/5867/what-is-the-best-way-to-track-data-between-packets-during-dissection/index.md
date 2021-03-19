+++
type = "question"
title = "What is the best way to track data between packets during dissection?"
description = '''In brief: What is the best way to track information between protocol packets during dissection?   More detail: Suppose I have a protocol which has multiple message types, some of which can only be fully dissected if certain information from another message is known (example below). I could just have...'''
date = "2011-08-25T07:07:00Z"
lastmod = "2011-08-25T07:33:00Z"
weight = 5867
keywords = [ "development", "dissector" ]
aliases = [ "/questions/5867" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the best way to track data between packets during dissection?](/questions/5867/what-is-the-best-way-to-track-data-between-packets-during-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5867-score" class="post-score" title="current number of votes">0</div><span id="post-5867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>In brief:</strong> What is the best way to track information between protocol packets during dissection?</p><p><strong>More detail:</strong> Suppose I have a protocol which has multiple message types, some of which can only be fully dissected if certain information from another message is known (example below). I could just have a <code>static gint</code> variable in my dissector that I update when data comes in, but this feels a little clunky. What is the best way to track this information so that dissection directed properly?</p><pre><code>/* Message One &quot;configuration&quot; */
struct conf_mesg {
    guint8 configuration; /* 0==Type_foo, 1==Type_bar, etc. */
};

/* Message Two &quot;data*/
struct data_mesg {
    guint32 data;
    /* guint16, guint16 if configuarion==Type_foo */
    /* guint8, guint8, guint16 if configuration==Type_bar */
    ...
};</code></pre><p>At least one <code>conf_mesg</code> will come before a <code>data_mesg</code> in the protocol. The default behavior (where the <code>conf_mesg</code> was never seen or contained bogus data) should be to display the data field as a <code>guint32</code>. What is the best way to track what the <code>configuration</code> field of the last <code>conf_mesg</code> was during packet dissection?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '11, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5867" class="comments-container"></div><div id="comment-tools-5867" class="comment-tools"></div><div class="clear"></div><div id="comment-5867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5869"></span>

<div id="answer-container-5869" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5869-score" class="post-score" title="current number of votes">1</div><span id="post-5869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="multipleinterfaces has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think using Wireshark "conversations" is probably the way to go.</p><p>From doc/README.developer:</p><p>"In wireshark a conversation is defined as a series of data packets between two address:port combinations"</p><p>A dissector can use a conversation to store state information about that conversation.</p><p>See section 2.1 of doc/README.developer for the details.</p><p>Keep in mind that Wireshark essentially does a first sequential dissection pass thru the capture file and then will re-dissect individual packets as the user selects particular packets.</p><p>So: If general information about the conversation ("config msg has been seen", etc) is not sufficient you may also need to store "per-packet" info to remember any decisions as to how to dissect a particular packet. See section 2.5 of doc/README.developer.</p><p>It's also probably worth spending a little time looking at some of the individual Wireshark dissectors to see how they use conversations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '11, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '11, 08:03</strong> </span></p></div></div><div id="comments-container-5869" class="comments-container"></div><div id="comment-tools-5869" class="comment-tools"></div><div class="clear"></div><div id="comment-5869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

