+++
type = "question"
title = "How do you use tshark with multiple ssl keys?"
description = '''I understand it&#x27;s possible to do SSL decryption with tshark by giving a key rule with the ssl.keys_list preferences option. However I&#x27;ve only seen examples with a single key, and I can&#x27;t find any real documentation for it. Is it possible to use tshark with multiple key rules, like you can in the Wir...'''
date = "2013-02-26T23:03:00Z"
lastmod = "2013-02-27T06:40:00Z"
weight = 18908
keywords = [ "ssl", "tshark", "decryption" ]
aliases = [ "/questions/18908" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do you use tshark with multiple ssl keys?](/questions/18908/how-do-you-use-tshark-with-multiple-ssl-keys)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18908-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand it's possible to do SSL decryption with <code>tshark</code> by giving a key rule with the <code>ssl.keys_list</code> preferences option. However I've only seen examples with a single key, and I can't find any real documentation for it. Is it possible to use <code>tshark</code> with multiple key rules, like you can in the Wireshark GUI?</p></div><div id="question-tags" class="tags-container tags">ssl tshark decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/f1f99b071794213796dcb33e787c5772?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakslice&#39;s gravatar image" /><p>rakslice<br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakslice has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '13, 23:03</p></div></div><div id="comments-container-18908" class="comments-container"></div><div id="comment-tools-18908" class="comment-tools"></div><div class="clear"></div><div id="comment-18908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18929"></span>

<div id="answer-container-18929" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18929-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's possible, and there are a couple of ways to go about it.</p><p>First, you can set the preferences on the CLI using the <code>-o</code> flag and a semi-colon to separate them like this:</p><pre><code>tshark -o &quot;ssl.keys_list:ip1,port1,proto1,key1;ip2;port2;proto2;key2&quot; ... (rest of your command)</code></pre><p>the "key" field is the path to the RSA Key file somewhere on disk.</p><p>Second, starting I think in Wireshark 1.8, whenever you configure SSL Decodes in the GUI, they are written to a file on disk in your Wireshark preferences directory (mac/linux that's ~/.wireshark/).</p><p>If you look in there at the <code>ssl_keys</code> file, you'll see all your keys listed. tshark respects this file when starting up, so you could configure multiple keys in the GUI, and then using tshark, it will inherit all of those same keys BY DEFAULT and you won't need to use the <code>-o</code> flag.</p><p>Have fun!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '13, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p>zachad<br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div></div><div id="comments-container-18929" class="comments-container"><span id="19256"></span><div id="comment-19256" class="comment"><div id="post-19256-score" class="comment-score">1</div><div class="comment-text"><p>One additional note: If you specify more than one key for a given IP address and port combination, only the last will be tried.</p></div><div id="comment-19256-info" class="comment-info"><span class="comment-age">(06 Mar '13, 18:50)</span> rakslice</div></div></div><div id="comment-tools-18929" class="comment-tools"></div><div class="clear"></div><div id="comment-18929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

