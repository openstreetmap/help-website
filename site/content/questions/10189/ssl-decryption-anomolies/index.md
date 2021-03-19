+++
type = "question"
title = "SSL Decryption Anomolies"
description = '''Still trying to use wiresharks SSL decryption service. I took Syn-Bits advise and used Data as the protocol decode for the SSL key. There are a few things I don&#x27;t understand. Why would the SSL dissector (or perhaps HTTP header decoder) document 2 data fields. The first data field is 1 byte long and ...'''
date = "2012-04-16T07:42:00Z"
lastmod = "2012-04-16T07:42:00Z"
weight = 10189
keywords = [ "ssl" ]
aliases = [ "/questions/10189" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption Anomolies](/questions/10189/ssl-decryption-anomolies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10189-score" class="post-score" title="current number of votes">0</div><span id="post-10189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Still trying to use wiresharks SSL decryption service. I took Syn-Bits advise and used Data as the protocol decode for the SSL key. There are a few things I don't understand.</p><p>Why would the SSL dissector (or perhaps HTTP header decoder) document 2 data fields. The first data field is 1 byte long and contains the ASCII letter G. The second data field starts off with ASCII letters ET followed by the remainder of HTTP header. If I combine the two data fields together, the HTTP GET headers looks fine.</p><p>For those that are more intimate with the design...what HTTP header (or SSL dissector) issues would result in the reporting of a "malformed packet"?? I can't see anything wrong and it went thru it byte by byte.</p><p>The Analyze Follow SSL Stream facility seems to report the proper HTTP Get and Response. My problem is that I'm trying to "programmatically automate" analysis and need to know the packet number of the GET packet. If its not in the "info" section of the gui display, I'm not sure how to get to the beginning of the http stream ?? If start analysis with the Response, I don't see the GET.</p><p>Advise/answers much appreciated..</p><p>thanks, Walter ================================================ I should add that the exact error message is:</p><pre><code>[Malformed Packet: GIF image]
  [Message: Malformed Packer (Exception occurred)]
  [Severity level: Error]
  [Group: Malformed]</code></pre><p>Is the G from my GET somehow being confused with the G for a gif file ?? Strange..</p><p>-wk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p><span>wakelt</span><br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '12, 12:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-10189" class="comments-container"></div><div id="comment-tools-10189" class="comment-tools"></div><div class="clear"></div><div id="comment-10189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

