+++
type = "question"
title = "How to write a pcap file with PyShark?"
description = '''I have a captured pcap file which I want to filter for a certain http host. Because I not only want the http packets I search first for the http streams and save their stream numbers. In a second step I filter the pcap file for these found stream numbers. Here ist what I do:   import pyshark  INFILE...'''
date = "2017-05-24T05:38:00Z"
lastmod = "2017-05-24T06:17:00Z"
weight = 61593
keywords = [ "python", "tshark", "pyshark" ]
aliases = [ "/questions/61593" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to write a pcap file with PyShark?](/questions/61593/how-to-write-a-pcap-file-with-pyshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61593-score" class="post-score" title="current number of votes">0</div><span id="post-61593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a captured pcap file which I want to filter for a certain http host. Because I not only want the http packets I search first for the http streams and save their stream numbers. In a second step I filter the pcap file for these found stream numbers.</p><p>Here ist what I do:</p><hr /><pre><code>import pyshark 
INFILE = &#39;./xy_2017-03-30.pcapng&#39;

def get_http_streams(host):
    pcap = pyshark.FileCapture(INFILE, only_summaries=False, display_filter=f&#39;http.host contains &quot;{host}&quot;&#39;)
    streams = set()
    for p in pcap:
        stream_nr = int(p.tcp.stream)
        streams.add(stream_nr)
    print()
    print(f&#39;Found {len(streams)} &quot;{host}&quot; streams.&#39;)
    return streams

s = get_http_streams(&#39;google&#39;) 
pcap = pyshark.FileCapture(INFILE)

pkt_list = [] 
print(&#39;Filtering...&#39;)
for i, p in enumerate(pcap):
    try:
        stream_nr = int(p.tcp.stream)
    except AttributeError:
        stream_nr = -1
    if stream_nr in s:
        pkt_list.append(p)

# -----------------------------------------------------------------------------
# How to write a pcap file now? pyshark.WriteFile(pkt_list, &#39;result.pcap&#39;) ?!
# -----------------------------------------------------------------------------

print(&#39;END&#39;)</code></pre><hr /><p>Now I have a list with the filtered packets. How would I write them out now to a new pcap file?</p><p>Thanks for any help!</p><p>Regards, Marcel</p><p>BTW: The captured pcap files are big (&gt; 300 MB). Scapy eats all my memory while reading...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-pyshark" rel="tag" title="see questions tagged &#39;pyshark&#39;">pyshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '17, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/c9aa89acedae622dfba3e1f7a8a4416b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mluethi&#39;s gravatar image" /><p><span>mluethi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mluethi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '17, 05:40</strong> </span></p></div></div><div id="comments-container-61593" class="comments-container"></div><div id="comment-tools-61593" class="comment-tools"></div><div class="clear"></div><div id="comment-61593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61594"></span>

<div id="answer-container-61594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61594-score" class="post-score" title="current number of votes">0</div><span id="post-61594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think saving a capture is supported. Regardless, pyshark is not part of the Wireshark project so you'll find support for pyshark over <a href="https://github.com/KimiNewt/pyshark/issues">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '17, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61594" class="comments-container"><span id="61596"></span><div id="comment-61596" class="comment"><div id="post-61596-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick reply! I saw other questions with PyShark and therefore tried to ask here. Will open an issue.</p><p>Do you think what I try so achieve would be possible with tshark alone?</p></div><div id="comment-61596-info" class="comment-info"><span class="comment-age">(24 May '17, 05:54)</span> <span class="comment-user userinfo">mluethi</span></div></div><span id="61598"></span><div id="comment-61598" class="comment"><div id="post-61598-score" class="comment-score"></div><div class="comment-text"><p>Not with tshark alone, you'll need some external scripting tool. The basic approach looks good, filter on the host required outputting the stream index (<code>-T fields -e tcp.stream</code>), then re-filter with those streams.</p></div><div id="comment-61598-info" class="comment-info"><span class="comment-age">(24 May '17, 06:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61594" class="comment-tools"></div><div class="clear"></div><div id="comment-61594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

