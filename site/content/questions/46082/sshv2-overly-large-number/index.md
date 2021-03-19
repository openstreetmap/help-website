+++
type = "question"
title = "SSHV2 Overly large number"
description = '''hello, can you explain to me the significance of this warning : &quot;Expert Information ( Warn / Protocol) : Overly large number&quot;'''
date = "2015-09-23T11:17:00Z"
lastmod = "2015-09-29T15:04:00Z"
weight = 46082
keywords = [ "large", "sshv2", "overly", "number" ]
aliases = [ "/questions/46082" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSHV2 Overly large number](/questions/46082/sshv2-overly-large-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46082-score" class="post-score" title="current number of votes">0</div><span id="post-46082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>can you explain to me the significance of this warning : "Expert Information ( Warn / Protocol) : Overly large number"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-sshv2" rel="tag" title="see questions tagged &#39;sshv2&#39;">sshv2</span> <span class="post-tag tag-link-overly" rel="tag" title="see questions tagged &#39;overly&#39;">overly</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '15, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/dd7c2fae79566e8fca3eadf168efe283?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rebanubtd&#39;s gravatar image" /><p><span>rebanubtd</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rebanubtd has no accepted answers">0%</span></p></div></div><div id="comments-container-46082" class="comments-container"></div><div id="comment-tools-46082" class="comment-tools"></div><div class="clear"></div><div id="comment-46082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46085"></span>

<div id="answer-container-46085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46085-score" class="post-score" title="current number of votes">1</div><span id="post-46085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to the code, that's the packet length in the key exchange.</p><p>File: packet-ssh.c - ssh_dissect_key_exchange()</p><pre><code>    plen = tvb_get_ntohl(tvb, offset) ;

    REMOVED CODE ....

    /*
     * Need to check plen &gt; 0x80000000 here
     */

    ti = proto_tree_add_uint(tree, hf_ssh_packet_length, tvb,
                    offset, 4, plen);
    if (plen &gt;= 0xffff) {
        expert_add_info_format(pinfo, ti, &amp;ei_ssh_packet_length, &quot;Overly large number %d&quot;, plen);
        plen = remain_length-4;
    }</code></pre><p>So, the SSH dissector checks if the packet length is larger than 0xffff. According to the <a href="https://tools.ietf.org/html/rfc4253">SSH RFC</a>, there is a <a href="https://tools.ietf.org/html/rfc4253#section-6.1">max packet length that MUST be supported</a> by any implementation, which is 32768 bytes (0x8000), and 'implementations SHOULD support longer packets, where they might be needed'.</p><p>So, I guess the check for 0xFFFF is an arbitrary max length chosen by the developer of the SSH dissector, probably based on the max size of a TCP segment.</p><p>Without the capture file, I can't say more than that ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '15, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46085" class="comments-container"><span id="46117"></span><div id="comment-46117" class="comment"><div id="post-46117-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer . How Can I Send you capture ?</p></div><div id="comment-46117-info" class="comment-info"><span class="comment-age">(24 Sep '15, 11:00)</span> <span class="comment-user userinfo">rebanubtd</span></div></div><span id="46118"></span><div id="comment-46118" class="comment"><div id="post-46118-score" class="comment-score"></div><div class="comment-text"><p>Load it into dropbox, google drive, etc. and post the link here.</p></div><div id="comment-46118-info" class="comment-info"><span class="comment-age">(24 Sep '15, 11:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46187"></span><div id="comment-46187" class="comment"><div id="post-46187-score" class="comment-score"></div><div class="comment-text"><p>ok</p><p><a href="https://drive.google.com/file/d/0B1TLQERSH3FSM1BIMVNJbmE3Mkk/view?usp=sharing">https://drive.google.com/file/d/0B1TLQERSH3FSM1BIMVNJbmE3Mkk/view?usp=sharing</a></p></div><div id="comment-46187-info" class="comment-info"><span class="comment-age">(26 Sep '15, 08:25)</span> <span class="comment-user userinfo">rebanubtd</span></div></div><span id="46237"></span><div id="comment-46237" class="comment"><div id="post-46237-score" class="comment-score"></div><div class="comment-text"><p>You can see "valid" values up until frame #16 and the frame length is in all cases part of the captured data.</p><p>I believe "something" is modifying the payload of the frames, because for some frames with "invalid" frame sizes, you also get <strong>unknown messages codes</strong>. So, either this is a totally modified SSH protocol (which I don't believe), or there is an error during frame transmission and/or during the capturing process.</p></div><div id="comment-46237-info" class="comment-info"><span class="comment-age">(28 Sep '15, 14:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46085" class="comment-tools"></div><div class="clear"></div><div id="comment-46085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46266"></span>

<div id="answer-container-46266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46266-score" class="post-score" title="current number of votes">1</div><span id="post-46266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The message "SSHV2 Overly large number" is due to slicing the packets to 100 byte. I have tested and reproduced it at home. The thing why evrything went fine until frame #16 is because in Frame #14 the key exchange is completed so far that the packets could be encrypted. And after that, the packet length is in accordance to the RFC(<a href="https://tools.ietf.org/html/rfc4253)">https://tools.ietf.org/html/rfc4253)</a> encrypted.</p><p>SSH Header (unsliced) of first Packet after the "Client: New Keys" packet. <img src="https://osqa-ask.wireshark.org/upfiles/SSH.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '15, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Sep '15, 12:29</strong> </span></p></div></div><div id="comments-container-46266" class="comments-container"><span id="46268"></span><div id="comment-46268" class="comment"><div id="post-46268-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have tested and reproduced it at home.<br />
...<br />
And after that, the packet length is in accordance to the RFC(<a href="https://tools.ietf.org/html/rfc4253)">https://tools.ietf.org/html/rfc4253)</a> encrypted</p></blockquote><p>O.K. good to know! Thanks.</p></div><div id="comment-46268-info" class="comment-info"><span class="comment-age">(29 Sep '15, 15:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46266" class="comment-tools"></div><div class="clear"></div><div id="comment-46266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

