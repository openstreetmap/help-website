+++
type = "question"
title = "HTTP gzip decompression failed (NOT out-of-order)"
description = '''As I was experimenting with wireshark and SSL decryption, I ran into a reproducible error. The SSL server sends back an HTML page and wireshark fails to decrypt: I get a frame HTTP/1.1 200 OK, inside of which: Content-encoded entity body (gzip): 77775 bytes [Error: Decompression failed]  I had a sim...'''
date = "2013-08-05T09:19:00Z"
lastmod = "2013-08-05T09:19:00Z"
weight = 23563
keywords = [ "gzip", "ssl" ]
aliases = [ "/questions/23563" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP gzip decompression failed (NOT out-of-order)](/questions/23563/http-gzip-decompression-failed-not-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23563-score" class="post-score" title="current number of votes">0</div><span id="post-23563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As I was experimenting with wireshark and SSL decryption, I ran into a reproducible error.</p><p>The SSL server sends back an HTML page and wireshark fails to decrypt:</p><p>I get a frame <code>HTTP/1.1 200 OK</code>, inside of which:</p><pre><code>Content-encoded entity body (gzip): 77775 bytes [Error: Decompression failed]</code></pre><p>I had a similar "Decompression failed" problem before with another server having to do with out-of-order frames, but in this capture everything is in-order.</p><p>I was able to reproduce this failure twice by going to<br />
<a href="https://www.chase.com"></a><a href="https://www.chase.com">https://www.chase.com</a><br />
Then scroll down to the bottom and click Site Map.<br />
You will get a properly decrypted main page, but not the "site map" page.</p><p>Here is the relevant captures with SSL keys<br />
<a href="http://cloudshark.org/captures/0b3b37e94edb">http://cloudshark.org/captures/0b3b37e94edb</a></p><p>SSL keys:<br />
<a href="http://pastebin.com/69V33BE2">http://pastebin.com/69V33BE2</a></p><p>Frame 1760 is where the failure happens.</p><p>Any suggestions on how to solve the failure?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gzip" rel="tag" title="see questions tagged &#39;gzip&#39;">gzip</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/5539b49a6661453d168b03c047917c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansmith&#39;s gravatar image" /><p><span>dansmith</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansmith has one accepted answer">50%</span> </br></br></p></div></div><div id="comments-container-23563" class="comments-container"></div><div id="comment-tools-23563" class="comment-tools"></div><div class="clear"></div><div id="comment-23563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

