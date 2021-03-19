+++
type = "question"
title = "Variable name in POST request"
description = '''Hello, I have capture a emission packet, and this is a HTTP/XML protocol using POST request. I saw the source code, but normaly, when we send a post request, we have to send a variable with its value to an url/server right ? So, how can I know the variable name or the multiple variable name use for ...'''
date = "2011-12-17T11:05:00Z"
lastmod = "2011-12-18T18:38:00Z"
weight = 8028
keywords = [ "variable", "post", "http" ]
aliases = [ "/questions/8028" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Variable name in POST request](/questions/8028/variable-name-in-post-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8028-score" class="post-score" title="current number of votes">0</div><span id="post-8028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have capture a emission packet, and this is a HTTP/XML protocol using POST request. I saw the source code, but normaly, when we send a post request, we have to send a variable with its value to an url/server right ? So, how can I know the variable name or the multiple variable name use for contact the serveur with a POST request ?</p><pre><code>POST /newsoap/soap/mim.php HTTP/1.1
Host: site.com
User-Agent: SITE/0.15 CFNetwork/548.0.3 Darwin/11.0.0
Content-Length: 1139
Accept: */*
Content-Type: text/xml; charset=utf-8
Accept-Language: fr-fr
Accept-Encoding: gzip, deflate
Cookie: PHPSESSID=20mgf6gtg00svvdg91mlh4t5e0
Connection: keep-alive

&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;soap:Envelope xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns:xsd=&quot;http://www.w3.org/2001/XMLSchema&quot; xmlns:soap=&quot;http://schemas.xmlsoap.org/soap/envelope/&quot;&gt;
&lt;soap:Body&gt;
&lt;requet xmlns=&quot;http://site.com/&quot;&gt;
&lt;lang&gt;fr&lt;/lang&gt;&lt;pass&gt;toto&lt;/pass&gt;
&lt;xml&gt;&lt;![CDATA[&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;Membrep nbInvitations=&quot;&quot; nbMessages=&quot;&quot; nbNews=&quot;&quot; enabled=&quot;&quot; nbCommunaute=&quot;&quot; nbEvenement=&quot;&quot; nbActivite=&quot;&quot; nbLieux=&quot;&quot; type_activite_id=&quot;&quot; creneau_val=&quot;&quot; activite_id=&quot;&quot; creneau_id=&quot;&quot; fonction=&quot;&quot; secteur=&quot;&quot; ville=&quot;&quot; genre=&quot;&quot; daten=&quot;&quot; Added=&quot;&quot; PK=&quot;&quot; activiteImage=&quot;&quot; activiteNiveau=&quot;&quot; activiteNom=&quot;&quot; statu=&quot;&quot; image=&quot;&quot; visible=&quot;&quot; facebookId=&quot;&quot; twitterId=&quot;&quot; linkedId=&quot;&quot; telephone=&quot;&quot; email=&quot;&quot; prenom=&quot;&quot; nom=&quot;&quot;&gt;&lt;listeElements/&gt;&lt;Positionp nom=&quot;&quot; PK=&quot;&quot; type=&quot;&quot; longitude=&quot;&quot; latitude=&quot;&quot;/&gt;&lt;/Membrep&gt;
]]&gt;&lt;/xml&gt;
&lt;nomrequet&gt;inscription&lt;/nomrequet&gt;
&lt;param1&gt;&lt;![CDATA[fr]]&gt;&lt;/param1&gt;
&lt;param2&gt;&lt;![CDATA[AAAAAA]]&gt;&lt;/param2&gt;
&lt;param3&gt;&lt;![CDATA[BBBBBBB]]&gt;&lt;/param3&gt;
&lt;param4&gt;&lt;![CDATA[CCCCCC]]&gt;&lt;/param4&gt;
&lt;param5&gt;&lt;![CDATA[DDDDDD]]&gt;&lt;/param5&gt;
&lt;param6&gt;&lt;![CDATA[EEEEEEEE]]&gt;&lt;/param6&gt;
&lt;/requet&gt;
&lt;/soap:Body&gt;
&lt;/soap:Envelope&gt;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '11, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/dbe9c012ae50b5436e46f4e39a2a6e7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rian&#39;s gravatar image" /><p><span>Rian</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Dec '11, 11:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8028" class="comments-container"></div><div id="comment-tools-8028" class="comment-tools"></div><div class="clear"></div><div id="comment-8028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8034"></span>

<div id="answer-container-8034" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8034-score" class="post-score" title="current number of votes">1</div><span id="post-8034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://tools.ietf.org/html/rfc2616#section-9.5">Section 9.5 "POST" of RFC 2616</a> says</p><blockquote><p>The actual function performed by the POST method is determined by the server and is usually dependent on the Request-URI. The posted entity is subordinate to that URI in the same way that a file is subordinate to a directory containing it, a news article is subordinate to a newsgroup to which it is posted, or a record is subordinate to a database.</p></blockquote><p>It says nothing about variables; the way the server responds to the request is, as indicated, dependent on the Request-URI (<code>/newsoap/soap/mim.php</code>) - perhaps that's a PHP script that reads an XML blob of <a href="http://en.wikipedia.org/wiki/SOAP">SOAP</a> (as opposed to a bar of soap :-)) and performs the request indicated by the blob with the parameters indicated by the blob.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '11, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8034" class="comments-container"></div><div id="comment-tools-8034" class="comment-tools"></div><div class="clear"></div><div id="comment-8034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

