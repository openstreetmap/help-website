+++
type = "question"
title = "JSON response full of dots &quot;.&quot; after &#x27;Follow TCP Stream&#x27;"
description = '''I&#x27;m trying to follow a JSON response but it shows it offuscated, this is the full Raw TCP Stream Wireshark is showing me: GET /api/v1/dependencies?gems=boolean_class,bundler,rake HTTP/1.1 Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3 Accept: */* User-Agent: bundler/1.5.0.rc.1 rubygems/2.1...'''
date = "2013-12-01T08:32:00Z"
lastmod = "2013-12-03T10:18:00Z"
weight = 27607
keywords = [ "encoding" ]
aliases = [ "/questions/27607" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JSON response full of dots "." after 'Follow TCP Stream'](/questions/27607/json-response-full-of-dots-after-follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27607-score" class="post-score" title="current number of votes">0</div><span id="post-27607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to follow a JSON response but it shows it offuscated, this is the full Raw TCP Stream Wireshark is showing me:</p><pre><code>GET /api/v1/dependencies?gems=boolean_class,bundler,rake HTTP/1.1
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept: */*
User-Agent: bundler/1.5.0.rc.1 rubygems/2.1.11 ruby/2.0.0 (x86_64-unknown-linux-gnu) command/install 273d73b77583ab06
Connection: keep-alive
Keep-Alive: 30
Host: 127.0.1.1:3132

HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8
X-Powered-By: geminabox 0.12.1
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Length: 750

..[.{.:.nameI&quot;.boolean_class.:.ET:.numberI&quot;
0.0.3.;.T:
platformI&quot;.ruby.;.F:.dependencies[.{.;.I&quot;.rake.;.T;.I&quot;.10.1.0.;.T;.I&quot;.ruby.;.F;.[.{.;.I&quot;
rspec.;.T;.I&quot;.2.14.1.;.T;.I&quot;.ruby.;.F;.[.[.I&quot;.rspec-core.;.TI&quot;.~&gt; 2.14.0.;.F[.I&quot;.rspec-expectations.;.TI&quot;.~&gt; 2.14.0.;.F[.I&quot;.rspec-mocks.;....................... etc .........</code></pre><p>I tried ASCII what got the same.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/d65593e3a584ff801c331e387964c69e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elgalu&#39;s gravatar image" /><p><span>elgalu</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elgalu has no accepted answers">0%</span></p></div></div><div id="comments-container-27607" class="comments-container"></div><div id="comment-tools-27607" class="comment-tools"></div><div class="clear"></div><div id="comment-27607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27609"></span>

<div id="answer-container-27609" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27609-score" class="post-score" title="current number of votes">1</div><span id="post-27609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="elgalu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The dots are "non-printable" characters (i.e. there is no ASCII representation of them). They are likely to be binary data values. The hex display pane will show the the exact values.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '13, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27609" class="comments-container"><span id="27611"></span><div id="comment-27611" class="comment"><div id="post-27611-score" class="comment-score"></div><div class="comment-text"><p>You are right <span>@grahamb</span> !! i wrongly assumed it was text.</p><p>If i wget it then open the binary file using Sublime Text with utf-8 encoding somehow it figures what the symbols mean:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/not-json.png" alt="alt text" /></p><p>Perhaps as a nice to have feature Wireshark may show this utf-8 symbols instead of converting them to dots "."</p></div><div id="comment-27611-info" class="comment-info"><span class="comment-age">(01 Dec '13, 09:23)</span> <span class="comment-user userinfo">elgalu</span></div></div><span id="27612"></span><div id="comment-27612" class="comment"><div id="post-27612-score" class="comment-score"></div><div class="comment-text"><p>You are right!! Perhaps as a nice to have feature Wireshark may show this utf-8 symbols instead of converting them to dots "." See Sublime Text screenshot below. Thanks!</p></div><div id="comment-27612-info" class="comment-info"><span class="comment-age">(01 Dec '13, 09:24)</span> <span class="comment-user userinfo">elgalu</span></div></div><span id="27613"></span><div id="comment-27613" class="comment"><div id="post-27613-score" class="comment-score">1</div><div class="comment-text"><p>Actually, the things such as EOT, BS, ACK &amp; etc are just the ASCII names for certain ASCII non-printing ("control") characters. Some of the names (e.g., ACK, DC1, DC2) are basically historical and others are things like (BS [backspace], VT [vertical tab]); In any case the names probably don't reflect the actual meaning/usage of the underlying binary value.</p><p>IOW: this has nothing to do with UTF-8.</p></div><div id="comment-27613-info" class="comment-info"><span class="comment-age">(01 Dec '13, 09:36)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="27614"></span><div id="comment-27614" class="comment"><div id="post-27614-score" class="comment-score"></div><div class="comment-text"><p>Thanks for all the clarifications! Very helpful.</p></div><div id="comment-27614-info" class="comment-info"><span class="comment-age">(01 Dec '13, 09:39)</span> <span class="comment-user userinfo">elgalu</span></div></div><span id="27615"></span><div id="comment-27615" class="comment"><div id="post-27615-score" class="comment-score"></div><div class="comment-text"><p>The reason why there are non-printable characters is: that's not JSON. It looks like BSON (binary JSON), which contains 'binary characters/values' as the name already implies.</p><p>Regards<br />
Kurt</p></div><div id="comment-27615-info" class="comment-info"><span class="comment-age">(01 Dec '13, 10:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27724"></span><div id="comment-27724" class="comment not_top_scorer"><div id="post-27724-score" class="comment-score"></div><div class="comment-text"><p>After digging into the source code i realized it was Ruby binary serialized data through <a href="http://www.ruby-doc.org/core-2.0.0/Marshal.html">Marshal</a> easily deserialized through <code>Marshal.load(File.open('not-json.binary'))</code></p><pre><code>Marshal.load(File.open(&#39;not-json.binary&#39;)) #=&gt;

[ {:name=&gt;&quot;boolean_class&quot;, :number=&gt;&quot;0.0.3&quot;, :platform=&gt;&quot;ruby&quot;, :dependencies=&gt;[]}, 
  {:name=&gt;&quot;rake&quot;, :number=&gt;&quot;10.1.0&quot;, :platform=&gt;&quot;ruby&quot;, :dependencies=&gt;[]},
  {:name=&gt;&quot;rspec&quot;, :number=&gt;&quot;2.14.1&quot;, :platform=&gt;&quot;ruby&quot;, :dependencies=&gt; [
    [&quot;rspec-core&quot;, &quot;~&gt; 2.14.0&quot;], [&quot;rspec-expectations&quot;, &quot;~&gt; 2.14.0&quot;], [&quot;rspec-mocks&quot;, &quot;~&gt; 2.14.0&quot;]
  ]}
]</code></pre></div><div id="comment-27724-info" class="comment-info"><span class="comment-age">(03 Dec '13, 10:18)</span> <span class="comment-user userinfo">elgalu</span></div></div></div><div id="comment-tools-27609" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-27609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

