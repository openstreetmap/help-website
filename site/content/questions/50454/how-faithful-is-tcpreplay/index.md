+++
type = "question"
title = "[closed] How faithful is tcpreplay"
description = '''I have a massive capture file which I would like to experiment by playing back on an interface using tcp replay, but I would like to know what to expect in terms of faithfulness of the replay keeping in mind facts that file is massive arounf 4 Gb, and I would like to compare its performance with oth...'''
date = "2016-02-23T19:06:00Z"
lastmod = "2016-02-24T02:52:00Z"
weight = 50454
keywords = [ "tcpreplay", "bittwist" ]
aliases = [ "/questions/50454" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How faithful is tcpreplay](/questions/50454/how-faithful-is-tcpreplay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50454-score" class="post-score" title="current number of votes">0</div><span id="post-50454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a massive capture file which I would like to experiment by playing back on an interface using tcp replay, but I would like to know what to expect in terms of faithfulness of the replay keeping in mind facts that file is massive arounf 4 Gb, and I would like to compare its performance with other replay tools like bittwist, so I need a way to start both of them to synchronize before replay. I know conventionally could just start the replay at the same time . but that seems naive to do am looking for a cleaner way to do so. Any suggestions are greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpreplay" rel="tag" title="see questions tagged &#39;tcpreplay&#39;">tcpreplay</span> <span class="post-tag tag-link-bittwist" rel="tag" title="see questions tagged &#39;bittwist&#39;">bittwist</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/81f68b9912ba0ebf8a5dcd0341036a71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networkstuff&#39;s gravatar image" /><p><span>networkstuff</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networkstuff has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>24 Feb '16, 02:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-50454" class="comments-container"><span id="50455"></span><div id="comment-50455" class="comment"><div id="post-50455-score" class="comment-score"></div><div class="comment-text"><p>tcpreplay is a most-virtuous, temperant process, and will hold fast to its reasoned understanding of the pcap file format in spite of circumstance such as a large packet capture size. :)</p><p>Do you have a specific question in mind when you ask about the "faithfulness" of the program? The FAQ may help? <a href="http://tcpreplay.synfin.net/wiki/FAQ">http://tcpreplay.synfin.net/wiki/FAQ</a></p><p>If you mean whether it honours timestamps or not, it does, but depends on how well-formatted the .pcap file you're reading into it is.</p></div><div id="comment-50455-info" class="comment-info"><span class="comment-age">(23 Feb '16, 20:52)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="50463"></span><div id="comment-50463" class="comment"><div id="post-50463-score" class="comment-score"></div><div class="comment-text"><p>This is a question for a tcpreplay support forum I think. not Wireshark Q&amp;A.</p></div><div id="comment-50463-info" class="comment-info"><span class="comment-age">(24 Feb '16, 02:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-50454" class="comment-tools"></div><div class="clear"></div><div id="comment-50454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 24 Feb '16, 02:52

</div>

</div>

</div>

