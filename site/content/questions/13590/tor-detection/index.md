+++
type = "question"
title = "TOR Detection"
description = '''Hello. Is there any way to determine from a basic Wireshaark trace if a TOR browser is being used? There&#x27;s the tell-tale signs of TCP and TLSv1 use, along with port 9001 and 9030. But having completed some tests - I&#x27;ve discovered this only worked once over 10 tests!! Any help would be appreciated.'''
date = "2012-08-13T09:30:00Z"
lastmod = "2012-08-14T03:09:00Z"
weight = 13590
keywords = [ "tor", "detection" ]
aliases = [ "/questions/13590" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TOR Detection](/questions/13590/tor-detection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13590-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>Is there any way to determine from a basic Wireshaark trace if a TOR browser is being used?</p><p>There's the tell-tale signs of TCP and TLSv1 use, along with port 9001 and 9030.</p><p>But having completed some tests - I've discovered this only worked once over 10 tests!!</p><p>Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags">tor detection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/bad885338a1b55b021a5426449cc44ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DustinCook&#39;s gravatar image" /><p>DustinCook<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DustinCook has no accepted answers">0%</span></p></div></div><div id="comments-container-13590" class="comments-container"></div><div id="comment-tools-13590" class="comment-tools"></div><div class="clear"></div><div id="comment-13590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13604"></span>

<div id="answer-container-13604" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13604-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>There's the tell-tale signs of TCP and TLSv1 use, along with port 9001 and 9030.</p></blockquote><p>Port 9030 is the directory server port. The client gets the list of nodes from the directory servers, if it does not have that list stored locally. So, you will see that traffic only, if the client was started for the first time, or after a long time.</p><p>Port 9001 is the default Tor Port, but many Nodes run on port 443 (or any other port). That is configurable. So, you will only see traffic on this port, if your clients talk to a Tor node with the default port settings.</p><blockquote><p>But having completed some tests - I've discovered this only worked once over 10 tests!!</p></blockquote><p>see above.</p><p>The best sign for Tor traffic is this:</p><ul><li><p>Look at the certificates. The Tor nodes will present a cert with a "random" name, like these:</p><blockquote><p><code>www.wgmyv7mbm6phnpq.net</code><br />
<code>www.istzu7bz6fzy2y7if.com</code></p></blockquote></li><li><p>Check the Lifetime of the cert. Tor certs are often valid for one year, starting with the current day (weak criteria).</p></li></ul><blockquote><p><code>notBefore: utcTime (0)   utcTime: 12-08-14 07:51:17 (UTC)</code><br />
<code>notAfter: utcTime (0)    utcTime: 13-08-14 07:51:17 (UTC)</code><br />
</p></blockquote><p>Using tshark, you can find this information as follows:</p><blockquote><p><code>tshark -r tor_traffic.cap -T fields -R "ssl.handshake.certificate" -e x509af.utcTime -e x509s at.printableString</code><br />
</p></blockquote><p>Sample output</p><blockquote><p><code>12-08-14 09:02:40 (UTC),13-08-14 09:02:40 (UTC) www.esvo7ripgfcpkpbhl.com,www.j6l4qj5dfvjlkxya.net</code><br />
<code>12-08-14 09:14:08 (UTC),13-08-14 09:14:08 (UTC) www.voej7w7i5wqhd.com,www.nhbrobe2u5.net</code><br />
<code>12-08-14 08:08:27 (UTC),13-08-14 08:08:27 (UTC) www.fgzxrfhrgo.net,www.too3xofkwpprvxix.net</code><br />
<code>12-08-14 07:38:26 (UTC),13-08-14 07:38:26 (UTC) www.3fcvwc4udn7mwj.net,www.iwajitj5g.net</code><br />
<code>12-08-14 08:36:16 (UTC),13-08-14 08:36:16 (UTC) www.gf2afmvv3jl6dg.net,www.lvdvho3yglfu6.net</code><br />
<code>12-08-14 08:48:34 (UTC),13-08-14 08:48:34 (UTC) www.gyk2lv67szubbg4ilq.com,www.ujasp2f6.net</code><br />
<code>12-08-14 09:00:19 (UTC),13-08-14 09:00:19 (UTC) www.b3dthjkqi6py.com,www.qi5itnnxft3l.net</code><br />
<code>12-08-14 07:40:36 (UTC),13-08-14 07:40:36 (UTC) www.cwrtpgdwvfo.com,www.b2h4tpc5fxaq4l.net</code><br />
<code>12-08-14 07:45:00 (UTC),13-08-14 07:45:00 (UTC) www.swxvuwbkux5ws.com,www.vlrzxyc7lyjcjqxv.net</code><br />
<code>12-08-14 08:03:23 (UTC),13-08-14 08:03:23 (UTC) www.vxlyzz7hhbo7reiwg.com,www.tq2bi77acv.net</code><br />
<code>12-08-14 08:01:07 (UTC),13-08-14 08:01:07 (UTC) www.5syfc6b7xph5.com,www.lqr4alfcyz.net</code><br />
<code>12-08-14 07:51:17 (UTC),13-08-14 07:51:17 (UTC) www.istzu7bz6fzy2y7if.com,www.wgmyv7mbm6phnpq.net</code><br />
<code>12-08-14 08:12:22 (UTC),13-08-14 08:12:22 (UTC) www.hrz7noiicfhnnr3w3s.com,www.gixyoknsh7udrxu.net</code><br />
</p></blockquote><p>Now, use a script to check the cert lifetime (1 year, start: today) and the structure of the cert names (more or less random).</p><p><strong>HINT</strong>: If the Tor node runs on a port that is not dissected as SSL/TLS, you need to add the port to the SSL properties, otherwise you won't see the cert and the lifetime!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13604" class="comments-container"></div><div id="comment-tools-13604" class="comment-tools"></div><div class="clear"></div><div id="comment-13604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

