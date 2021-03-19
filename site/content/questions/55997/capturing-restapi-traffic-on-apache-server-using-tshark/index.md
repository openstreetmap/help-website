+++
type = "question"
title = "capturing RESTAPI traffic on apache server using tshark"
description = '''Is it possible to capture incoming REST API requests to an tomcat server, in order to validate whether external clients are using proper credentials. 401 responses are produced but we need to prove that the REST API is not the problem but rather the requests. We do however have an haproxy handling i...'''
date = "2016-09-29T15:05:00Z"
lastmod = "2016-09-29T15:05:00Z"
weight = 55997
keywords = [ "api", "tshark", "tcp" ]
aliases = [ "/questions/55997" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing RESTAPI traffic on apache server using tshark](/questions/55997/capturing-restapi-traffic-on-apache-server-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55997-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to capture incoming REST API requests to an tomcat server, in order to validate whether external clients are using proper credentials. 401 responses are produced but we need to prove that the REST API is not the problem but rather the requests. We do however have an haproxy handling incoming requests so not sure if this will work. If it is possible, how do we do this?</p><pre><code>tshark -f &quot;tcp port 22&quot; -w /tmp/capture.txt</code></pre></div><div id="question-tags" class="tags-container tags">api tshark tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '16, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/3e2a73b340277a2e2ec80657bebc50a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbieShark&#39;s gravatar image" /><p>newbieShark<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbieShark has no accepted answers">0%</span></p></div></div><div id="comments-container-55997" class="comments-container"></div><div id="comment-tools-55997" class="comment-tools"></div><div class="clear"></div><div id="comment-55997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

