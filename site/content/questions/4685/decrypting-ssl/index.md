+++
type = "question"
title = "Decrypting SSL"
description = '''I am using wireshark 1.6. I am trying to decrypt an SSL stream on a capture from one of our production servers. I have a capture taken from that server. I have the key extacted in pks format. I have converted it to pkcs12 and then RSA to remove the password. I also tried onverting to pcks8 but no lu...'''
date = "2011-06-22T19:20:00Z"
lastmod = "2011-06-23T12:02:00Z"
weight = 4685
keywords = [ "decryption", "ssl" ]
aliases = [ "/questions/4685" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting SSL](/questions/4685/decrypting-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4685-score" class="post-score" title="current number of votes">0</div><span id="post-4685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark 1.6. I am trying to decrypt an SSL stream on a capture from one of our production servers. I have a capture taken from that server. I have the key extacted in pks format. I have converted it to pkcs12 and then RSA to remove the password. I also tried onverting to pcks8 but no luck. I configured my ssl preferences to "serveraddress,443,http,c:certcc.pem". I also tried adding it to the RSA key list in multiple formats.</p><p>All of the examples I find reference creating your own cert but I dont see how this would work in a production environment that is using a verisign cert.</p><p>What am I missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '11, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/bdbf9eb175760c2fdcab4d7a2187945c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ericinsd&#39;s gravatar image" /><p><span>ericinsd</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ericinsd has no accepted answers">0%</span></p></div></div><div id="comments-container-4685" class="comments-container"></div><div id="comment-tools-4685" class="comment-tools"></div><div class="clear"></div><div id="comment-4685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4689"></span>

<div id="answer-container-4689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4689-score" class="post-score" title="current number of votes">2</div><span id="post-4689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6032">a bug has been reported</a> with version 1.6.0 which seems to indicate that Wireshark needs to be restarted before the SSL settings take effect (which was not necessary before), but I haven't verified that yet.</p><p>Then, there might be other reasons why SSL decryption does not work for you. Here are the most common ones:</p><ol><li>The private key is not in the right format or does not match the certificate from the server.</li><li>The SSL session was reused and the full SSL handshake is not in the tracefile.</li><li>A DH cipher has been chosen by the server.</li></ol><p>You might want to check the presentation I have given at Sharkfest'09 about <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">troubleshooting SSL with Wireshark</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '11, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4689" class="comments-container"><span id="4693"></span><div id="comment-4693" class="comment"><div id="post-4693-score" class="comment-score"></div><div class="comment-text"><p>Thank you. It does appear that Wireshark does need to be restarted. By adding the original pfx file with its password to the RSA key list I was successful.</p><p>I now see all of the data returned by our application but I do not see the full post from the client. Is this normal?</p><p>Thank you! Eric</p></div><div id="comment-4693-info" class="comment-info"><span class="comment-age">(23 Jun '11, 07:16)</span> <span class="comment-user userinfo">ericinsd</span></div></div><span id="4694"></span><div id="comment-4694" class="comment"><div id="post-4694-score" class="comment-score"></div><div class="comment-text"><p>(converted your answer to a comment, see the FAQ)</p><p>Glad you got a step further. However, you should be able to see both client and server traffic decrypted, so something else is still not OK. Are you able to share the trace and the key? Or is it not from a test environment? If you want to, you can send them to me privately (see my profile for my address).</p></div><div id="comment-4694-info" class="comment-info"><span class="comment-age">(23 Jun '11, 08:37)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4696"></span><div id="comment-4696" class="comment"><div id="post-4696-score" class="comment-score"></div><div class="comment-text"><p>It is from a Production application that contains NPPI so...unfortunately I cannot. It is actually a system to system interface that posts and XML request and returns an XML response. I actually see the post.....but not the request contained in the post. The client communication looks like this:</p><p>POST /CGI-BIN/CCListener.exe HTTP/1.1</p><p>Content-type: text/xml</p><p>OPTR_CXT: 01000100000f62ef4d-7401-48ea-b24e-76f89de5a1472c5c5b42-1a87-4076-92e0-2a31ee74396a2266 HTTP ;</p><p>User-Agent: Jakarta Commons-HttpClient/2.0final</p><p>Host: www.I obscured the URL.com</p><p>Content-Length: 1504</p><p><strong>After this I see our server's resonse but I dont see the data that was posted? Our system could not generate a reply unless it received a request with the above post</strong></p></div><div id="comment-4696-info" class="comment-info"><span class="comment-age">(23 Jun '11, 10:12)</span> <span class="comment-user userinfo">ericinsd</span></div></div><span id="4706"></span><div id="comment-4706" class="comment"><div id="post-4706-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment" again, please review the FAQ)</p><p>You might want to fiddle with the SSL and HTTP protocol preferences regarding reassembly. Also, it might be a bug in Wireshark. Are there more POST requests with data in the same TCP session? Do subsequent requests show as "Application Data"?</p></div><div id="comment-4706-info" class="comment-info"><span class="comment-age">(23 Jun '11, 12:02)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-4689" class="comment-tools"></div><div class="clear"></div><div id="comment-4689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

