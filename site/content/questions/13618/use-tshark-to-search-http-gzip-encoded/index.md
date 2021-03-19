+++
type = "question"
title = "Use tshark to search http gzip encoded"
description = '''So...topic says it. I&#x27;m attempting to do something like ngrep (which for some reason isn&#x27;t working on my pcaps). I&#x27;m trying to search for an item in a gzip encoded pcap, but I&#x27;m having a rough go of it. Here&#x27;s what I&#x27;ve tried: tshark -o http.decompress_body:TRUE -r _test.pcap -R &#x27;data-text-lines con...'''
date = "2012-08-14T10:22:00Z"
lastmod = "2012-08-14T10:39:00Z"
weight = 13618
keywords = [ "gzipped" ]
aliases = [ "/questions/13618" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Use tshark to search http gzip encoded](/questions/13618/use-tshark-to-search-http-gzip-encoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13618-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So...topic says it. I'm attempting to do something like ngrep (which for some reason isn't working on my pcaps). I'm trying to search for an item in a gzip encoded pcap, but I'm having a rough go of it. Here's what I've tried:</p><p>tshark -o http.decompress_body:TRUE -r _test.pcap -R 'data-text-lines contains Commentary'</p><p>But it's not seeming to fly. Any hints on how to look into an http body that's gzip'ed with tshark? I know I can do this with wireshark, but I'd like to do it with tshark on a remote machine. Thank you.</p></div><div id="question-tags" class="tags-container tags">gzipped</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/37898d970fb9980bdd2168e913a50ca2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngel&#39;s gravatar image" /><p>DigiAngel<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngel has no accepted answers">0%</span></p></div></div><div id="comments-container-13618" class="comments-container"></div><div id="comment-tools-13618" class="comment-tools"></div><div class="clear"></div><div id="comment-13618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13620"></span>

<div id="answer-container-13620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13620-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seems to work fine with me:</p><pre><code>$ tshark -o http.decompress_body:FALSE -nlr http-compression-ipv6.pcap -R &#39;data-text-lines contains &quot;apply&quot;&#39;
$ tshark -o http.decompress_body:TRUE -nlr http-compression-ipv6.pcap -R &#39;data-text-lines contains &quot;apply&quot;&#39;
 90   6.221425 2a00:1450:4007:802::101f -&gt; 2001:980:5354:3:fa1e:dfff:fed8:8748 HTTP 721 HTTP/1.1 200 OK  (text/html)
$</code></pre><p>Do you have the following settings:</p><ul><li>IP checksum checking disabled</li><li>TCP checksum checking disabled</li><li>Full packets, so captures with no snaplength</li><li>TCP reassembly enabled</li><li>HTTP reassembly enabled</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Aug '12, 10:40</p></div></div><div id="comments-container-13620" class="comments-container"><span id="13629"></span><div id="comment-13629" class="comment"><div id="post-13629-score" class="comment-score"></div><div class="comment-text"><p>Yea that TOTALLY works...I think I needed to define my data-text-lines in single quotes..just what the doctor ordered...thank you.</p></div><div id="comment-13629-info" class="comment-info"><span class="comment-age">(14 Aug '12, 12:15)</span> DigiAngel</div></div><span id="13644"></span><div id="comment-13644" class="comment"><div id="post-13644-score" class="comment-score"></div><div class="comment-text"><p>Also please note that "contains" is case sensitive in the current version of Wireshark. It might not be in the future (as discussed at Sharkfest'12).</p></div><div id="comment-13644-info" class="comment-info"><span class="comment-age">(15 Aug '12, 00:43)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-13620" class="comment-tools"></div><div class="clear"></div><div id="comment-13620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

