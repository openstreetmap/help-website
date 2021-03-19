+++
type = "question"
title = "Unicode Support &amp; Extended 8-Bit Ascii"
description = '''I&#x27;m disappointed that Wireshark doesn&#x27;t seem to support Unicode or 8-bit ASCII. I can understand Unicode is difficult to parse because each character isn&#x27;t represented by a fixed number of bytes, but I don&#x27;t see the excuse for not having 8-bit ASCII. In any case, Unicode is the future, a lot of webp...'''
date = "2010-10-02T18:00:00Z"
lastmod = "2010-10-02T18:00:00Z"
weight = 405
keywords = [ "iso", "8859", "extended", "ascii", "unicode" ]
aliases = [ "/questions/405" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unicode Support & Extended 8-Bit Ascii](/questions/405/unicode-support-extended-8-bit-ascii)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-405-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm disappointed that Wireshark doesn't seem to support Unicode or 8-bit ASCII. I can understand Unicode is difficult to parse because each character isn't represented by a fixed number of bytes, but I don't see the excuse for not having 8-bit ASCII.</p><p>In any case, Unicode is the future, a lot of webpages are using it already and they come up as gibberish in Wireshark. If you follow a TCP stream there is even an option for viewing the now obsolete EBCDIC but no Unicode.</p></div><div id="question-tags" class="tags-container tags">iso 8859 extended ascii unicode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '10, 18:00</strong></p><img src="https://secure.gravatar.com/avatar/773762053fcc91fb86dd50ea9a1595fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eventual%20Zen&#39;s gravatar image" /><p>Eventual Zen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eventual Zen has no accepted answers">0%</span></p></div></div><div id="comments-container-405" class="comments-container"><span id="409"></span><div id="comment-409" class="comment"><div id="post-409-score" class="comment-score">2</div><div class="comment-text"><p>And the question is?</p></div><div id="comment-409-info" class="comment-info"><span class="comment-age">(03 Oct '10, 13:44)</span> Jaap ♦</div></div><span id="446"></span><div id="comment-446" class="comment"><div id="post-446-score" class="comment-score">1</div><div class="comment-text"><p>See the first item in</p><pre><code>http://wiki.wireshark.org/Development/Wishlist#Dissector_infrastructure</code></pre><p>There's a significant amount of work involved in doing it right.</p></div><div id="comment-446-info" class="comment-info"><span class="comment-age">(06 Oct '10, 14:34)</span> Guy Harris ♦♦</div></div><span id="448"></span><div id="comment-448" class="comment"><div id="post-448-score" class="comment-score"></div><div class="comment-text"><p>Note also that "Follow TCP Stream" is sort of "dumb by design", in that it just dumps raw TCP payload. To do more than just printable {ASCII,EBCDIC} (note, BTW, that EBCDIC wasn't obsolete when that capability was added, as somebody found that useful enough to implement...), either it would need to hook into subdissectors, so that it would see the payload as more than just a pile of octets, or there would need to be "Follow HTTP conversation" etc. that hook into the subdissectors.</p></div><div id="comment-448-info" class="comment-info"><span class="comment-age">(06 Oct '10, 16:08)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-405" class="comment-tools"></div><div class="clear"></div><div id="comment-405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

