+++
type = "question"
title = "Question about fix.sendingTime for FIX Protocol"
description = '''Hi All, I am using FIX Dissector to decode FIX Protocol, and I got following message. SendingTime (52): 20120927-19:28:04.909 I am sure there should be 6 digits for milliseconds and microseconds, for instance, 19:28:04.909XXX. Can I show the all 6 digits by changing some settings? Thanks.'''
date = "2012-09-28T07:49:00Z"
lastmod = "2016-02-09T22:02:00Z"
weight = 14594
keywords = [ "fix" ]
aliases = [ "/questions/14594" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Question about fix.sendingTime for FIX Protocol](/questions/14594/question-about-fixsendingtime-for-fix-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14594-score" class="post-score" title="current number of votes">0</div><span id="post-14594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am using FIX Dissector to decode FIX Protocol, and I got following message.</p><p><strong>SendingTime (52): 20120927-19:28:04.909</strong></p><p>I am sure there should be 6 digits for milliseconds and microseconds, for instance, 19:28:04.909XXX. Can I show the all 6 digits by changing some settings?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/cd57e360702cc9f1c2d3f26661ec776e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylin&#39;s gravatar image" /><p><span>ylin</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylin has no accepted answers">0%</span></p></div></div><div id="comments-container-14594" class="comments-container"></div><div id="comment-tools-14594" class="comment-tools"></div><div class="clear"></div><div id="comment-14594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50039"></span>

<div id="answer-container-50039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50039-score" class="post-score" title="current number of votes">0</div><span id="post-50039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is great. Could you let me know how you are doing it, as I am not able to dissect it yet, I tried this program but its not working.</p><h1 id="section">------------------------------------------------------------------------------</h1><p>from scapy.all import *</p><p>def ExtractFIX(pcap): """A generator that iterates over the packets in a scapy pcap iterable and extracts the FIX messages. In the case where there are multiple FIX messages in one packet, yield each FIX message individually.""" for packet in pcap: if packet.haslayer('Raw'): # Only consider TCP packets which contain raw data. load = packet.getlayer('Raw').load</p><pre><code>        # Ignore raw data that doesn&#39;t contain FIX.
        if not &#39;FIX&#39; in load:
            continue

        # Replace \x01 with &#39;|&#39;.
        load = re.sub(r&#39;\x01&#39;, &#39;|&#39;, load)

        # Split out each individual FIX message in the packet by putting a 
        # &#39;;&#39; between them and then using split(&#39;;&#39;).
        for subMessage in re.sub(r&#39;\|8=FIX&#39;, &#39;|;8=FIX&#39;, load).split(&#39;;&#39;):
            # Yield each sub message. More often than not, there will only be one.
            assert subMessage[-1:] == &#39;|&#39;
            yield subMessage
    else:
        continue</code></pre><p>pcap = rdpcap('dump.pcap') for fixMessage in ExtractFIX(pcap): print fixMessage<br />
</p><h1 id="section-1">---------------------------------------------------------------------------------------</h1><p>And giving this error</p><p>pcap = rdpcap('dump.pcap') NameError: name 'rdpcap' is not defined process finished with exit code 1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/d20d7102fd9001359c35732770f6f143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fixmessenger&#39;s gravatar image" /><p><span>fixmessenger</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fixmessenger has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50039" class="comments-container"></div><div id="comment-tools-50039" class="comment-tools"></div><div class="clear"></div><div id="comment-50039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

