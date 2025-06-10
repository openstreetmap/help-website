+++
type = "question"
title = "ssl certificate verification failed"
description = '''I am running the three lines of code from the example on the command line and I am getting an SSL certificate verification failed error. Thanks for any help or suggestion.    from OSMPythonTools.api import Api api = Api() way = api.query(&#x27;way/5887599&#x27;) [api] downloading data: way/5887599 The request...'''
date = "2023-04-07T07:16:00Z"
lastmod = "2023-04-07T09:55:00Z"
weight = 87071
keywords = [ "newbie" ]
aliases = [ "/questions/87071" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ssl certificate verification failed](/questions/87071/ssl-certificate-verification-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87071-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running the three lines of code from the example on the command line and I am getting an SSL certificate verification failed error. Thanks for any help or suggestion.</p>
<blockquote>
<blockquote>
<blockquote>
<p>from OSMPythonTools.api import Api api = Api() way = api.query('way/5887599') [api] downloading data: way/5887599 The requested data could not be downloaded. Please check whether your internet connection is working. Traceback (most recent call last): File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py", line 1348, in do_open h.request(req.get_method(), req.selector, req.data, headers, File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 1282, in request self._send_request(method, url, body, headers, encode_chunked) File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 1328, in _send_request self.endheaders(body, encode_chunked=encode_chunked) File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 1277, in endheaders self._send_output(message_body, encode_chunked=encode_chunked) File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 1037, in _send_output self.send(msg) File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 975, in send self.connect() File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 1454, in connect self.sock = self._context.wrap_socket(self.sock, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py", line 517, in wrap_socket return self.sslsocket_class._create( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py", line 1075, in _create self.do_handshake() File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py", line 1346, in do_handshake self._sslobj.do_handshake() ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:992)</p>
</blockquote>
</blockquote>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '23, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/1fcad23c9e7a16ccc9e93aeb9dea99dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sartimk&#39;s gravatar image" />
<p><span>sartimk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sartimk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87071" class="comments-container">
<span id="87073"></span>
<div id="comment-87073" class="comment">
<div id="post-87073-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should invest the effort to format your question in a legible fashion if you want people to spend their spare time helping you.</p>
</div>
<div id="comment-87073-info" class="comment-info">
<span class="comment-age">(07 Apr '23, 08:37)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="87075"></span>
<div id="comment-87075" class="comment">
<div id="post-87075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://stackoverflow.com/help/how-to-ask">https://stackoverflow.com/help/how-to-ask</a> might be useful - explain more about what you are doing to help others to help you.</p>
</div>
<div id="comment-87075-info" class="comment-info">
<span class="comment-age">(07 Apr '23, 09:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87071-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

