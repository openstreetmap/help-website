+++
type = "question"
title = "A weird problem about LUA dissector: treeitem fails in IF condition"
description = '''this is a simple post dissector code... just add a new protofield with the string “blahblahblah” in the dissect tree. The weird thing is if the line “b2=10” is removed, the script works; if it exists, the scripts doesn’t work. b1=0 b2=0  myproto = Proto(&quot;myproto&quot;,&quot;test&quot;)  test_tag = ProtoField.strin...'''
date = "2016-02-18T22:45:00Z"
lastmod = "2016-07-22T08:31:00Z"
weight = 50325
keywords = [ "lua", "treeitem", "postdissector" ]
aliases = [ "/questions/50325" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [A weird problem about LUA dissector: treeitem fails in IF condition](/questions/50325/a-weird-problem-about-lua-dissector-treeitem-fails-in-if-condition)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50325-score" class="post-score" title="current number of votes">0</div><span id="post-50325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>this is a simple post dissector code... just add a new protofield with the string “blahblahblah” in the dissect tree.</p><p>The weird thing is if the line “b2=10” is removed, the script works; if it exists, the scripts doesn’t work.</p><pre><code>b1=0
b2=0

myproto = Proto(&quot;myproto&quot;,&quot;test&quot;)

test_tag = ProtoField.string(&quot;TestTag&quot;, &quot;testtag&quot;)

myproto.fields = {test_tag}

function myproto.dissector(tvb,pinfo,tree)
    local subtree = tree:add(myproto,&quot;My Test Protocol&quot;)

    if b1==b2 then
        subtree:add(test_tag, &quot;blahblahblah&quot;)
        b2=10
    end
end

register_postdissector(myproto,false)</code></pre><p>I have met this issue on stable version 2.0.1 and development versioni 2.1.0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-treeitem" rel="tag" title="see questions tagged &#39;treeitem&#39;">treeitem</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/bddac862940f1463a8442066ff05a0bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kylegzy&#39;s gravatar image" /><p><span>kylegzy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kylegzy has no accepted answers">0%</span></p></div></div><div id="comments-container-50325" class="comments-container"></div><div id="comment-tools-50325" class="comment-tools"></div><div class="clear"></div><div id="comment-50325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54241"></span>

<div id="answer-container-54241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54241-score" class="post-score" title="current number of votes">0</div><span id="post-54241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is expected behavior since Wireshark processes packets more than once. You can see the difference in behavior if you run <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> though, because <code>tshark</code> only processes packets once unless you explicitly tell it to perform a 2-pass analysis.</p><p>Compare:</p><pre><code>tshark -r myproto.pcap -O myproto</code></pre><p>with:</p><pre><code>tshark -r myproto.pcap -2O myproto</code></pre><p>In the first case, the first packet in <code>myproto.pcap</code> will display "<code>testtag: blahblahblah</code>", but since <code>b2</code> is then set to <code>10</code>, subsequent packets won't match the value of <code>b1</code>, <code>b1</code> being <code>0</code>, so the <code>testtag</code> isn't displayed for any other packets.</p><p>In the second case, all packets including the first packet will be processed more than once, so none of the packets will display the <code>testtag</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '16, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54241" class="comments-container"></div><div id="comment-tools-54241" class="comment-tools"></div><div class="clear"></div><div id="comment-54241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

