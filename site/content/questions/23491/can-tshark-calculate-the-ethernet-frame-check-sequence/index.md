+++
type = "question"
title = "Can tshark calculate the ethernet Frame Check Sequence?"
description = '''I&#x27;m writing a script where I need tshark to calculate the frame check sequence. I know I can output the existing FCS that is stored in the packet with: $ tshark -T fields -e eth.fcs -r input.cap  But if this FCS is wrong, can tshark calculate the correct one? In wireshark if I open a file where the ...'''
date = "2013-07-31T15:38:00Z"
lastmod = "2013-08-01T14:15:00Z"
weight = 23491
keywords = [ "frame", "fcs", "sequence", "tshark", "check" ]
aliases = [ "/questions/23491" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can tshark calculate the ethernet Frame Check Sequence?](/questions/23491/can-tshark-calculate-the-ethernet-frame-check-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23491-score" class="post-score" title="current number of votes">0</div><span id="post-23491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a script where I need tshark to calculate the frame check sequence. I know I can output the existing FCS that is stored in the packet with:</p><pre><code>$ tshark -T fields -e eth.fcs -r input.cap</code></pre><p>But if this FCS is wrong, can tshark calculate the correct one? In wireshark if I open a file where the FCS is wrong, wireshark tells me it's wrong and outputs the value that it <em>should</em> be. Can tshark output the value that it should be instead of just what is stored in the packet data?</p><p>Thanks, Jon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-fcs" rel="tag" title="see questions tagged &#39;fcs&#39;">fcs</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/e96b0196e8e968b1a2d8f6ddfda87ab1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lemurshark&#39;s gravatar image" /><p><span>Lemurshark</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lemurshark has no accepted answers">0%</span></p></div></div><div id="comments-container-23491" class="comments-container"><span id="23504"></span><div id="comment-23504" class="comment"><div id="post-23504-score" class="comment-score"></div><div class="comment-text"><p>Any help is appreciated. I wrote a script that would run several options from tshark to see if it would output the correct, calculated checksum instead of the checksum that is stored in the packet, but I haven't been able to find the right option.</p><pre><code>$ for option in $(tshark -G | grep -i &quot;fcs&quot; | awk &#39;{ for (i=2; i&lt;NF; i++) {if ($i ~ /.*\..*/) {print $i; next } } }&#39;); do echo $option; tshark -T fields -e $option -r onebadchecksum.cap 2&gt;/dev/null; done</code></pre><p>If I pull up the trace in wireshark, it tells me this:</p><pre><code>Frame check sequence: 0x665adc0c [incorrect, should be 0x509e1835]</code></pre><p>So wireshark knows what the correct value should be. Can tshark tell me the same thing?</p></div><div id="comment-23504-info" class="comment-info"><span class="comment-age">(01 Aug '13, 08:10)</span> <span class="comment-user userinfo">Lemurshark</span></div></div></div><div id="comment-tools-23491" class="comment-tools"></div><div class="clear"></div><div id="comment-23491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23512"></span>

<div id="answer-container-23512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23512-score" class="post-score" title="current number of votes">1</div><span id="post-23512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here is how you can view the calculated FCS with tshark:</p><pre><code>tshark -o eth.assume_fcs:TRUE -o eth.check_fcs:TRUE -r ethernet-frame-with-fcs.enc -V -O eth
Frame 1: 1518 bytes on wire (12144 bits), 1518 bytes captured (12144 bits)
Ethernet II, Src: OmronTat_0a:0a:02 (00:00:0a:0a:0a:02), Dst: OmronTat_0a:0a:01 (00:00:0a:0a:0a:01)
    Destination: OmronTat_0a:0a:01 (00:00:0a:0a:0a:01)
        Address: OmronTat_0a:0a:01 (00:00:0a:0a:0a:01)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: OmronTat_0a:0a:02 (00:00:0a:0a:0a:02)
        Address: OmronTat_0a:0a:02 (00:00:0a:0a:0a:02)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IP (0x0800)
    Frame check sequence: 0xf6979097 [incorrect, should be 0x09686f68]
        [FCS Good: False]
        [FCS Bad: True]
            [Expert Info (Error/Checksum): Bad checksum]
                [Message: Bad checksum]
                [Severity level: Error]
                [Group: Checksum]
Internet Protocol Version 4, Src: 10.10.10.2 (10.10.10.2), Dst: 10.10.10.1 (10.10.10.1)
Data (1480 bytes)</code></pre><p>I leave it as an exercise for the reader to extract the FCS from the output :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23512" class="comments-container"></div><div id="comment-tools-23512" class="comment-tools"></div><div class="clear"></div><div id="comment-23512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

