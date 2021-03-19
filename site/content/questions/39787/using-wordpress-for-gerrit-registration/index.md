+++
type = "question"
title = "Using WordPress for Gerrit Registration"
description = '''I posted to wireshark-dev but got no response. Sorry for the duplication. I am trying to register with Gerrit using WordPress. It does not work. It appears that the initial POST request is being redirected to use HTTP/S, and the redirect is using a GET instead of a POST. The process stalls at that p...'''
date = "2015-02-10T17:58:00Z"
lastmod = "2015-02-11T09:38:00Z"
weight = 39787
keywords = [ "wordpress", "gerrit" ]
aliases = [ "/questions/39787" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using WordPress for Gerrit Registration](/questions/39787/using-wordpress-for-gerrit-registration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39787-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I posted to wireshark-dev but got no response. Sorry for the duplication.</p><p>I am trying to register with Gerrit using WordPress. It does not work. It appears that the initial POST request is being redirected to use HTTP/S, and the redirect is using a GET instead of a POST. The process stalls at that point.</p><p>Am I missing something obvious, or is this a known issue? Who would be the contact to get this fixed?</p></div><div id="question-tags" class="tags-container tags">wordpress gerrit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/6a7bcd53f128960b7e664fa5ca309008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beastham&#39;s gravatar image" /><p>beastham<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beastham has no accepted answers">0%</span></p></div></div><div id="comments-container-39787" class="comments-container"><span id="39788"></span><div id="comment-39788" class="comment"><div id="post-39788-score" class="comment-score"></div><div class="comment-text"><p>Gerald Coombs (our fearless leader)is the Admin.</p><p>He's quite responsive to Admin issues, so I'm sure he'll respond as soon as he can.</p><p>You might also try asking this on a Gerrit forum since this sounds more like a Gerrit issue than a Wireshark issue.</p></div><div id="comment-39788-info" class="comment-info"><span class="comment-age">(10 Feb '15, 19:52)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-39787" class="comment-tools"></div><div class="clear"></div><div id="comment-39787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39802"></span>

<div id="answer-container-39802" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39802-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which Wordpress site are you trying to authenticate against (self-hosted, one at wordpress.com, ...)? Do you happen to know which OpenID plugin you're using?</p><p>I tried installing the simply-named "<a href="https://wordpress.org/plugins/openid/">OpenID</a>" plugin on blog.wireshark.org about a year ago and ran into the same sorts of issues that you're seeing. Unfortunately development on that plugin seems to be abandoned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-39802" class="comments-container"><span id="39803"></span><div id="comment-39803" class="comment"><div id="post-39803-score" class="comment-score"></div><div class="comment-text"><p>I am using <a href="https://code.wireshark.org/review/login/register,">https://code.wireshark.org/review/login/register,</a> and then clicking on the WordPress icon and entering my Wordpress.com user ID. Tracing the flow shows it communicating with WordPress, with the redirect appearing to cause the problem.</p></div><div id="comment-39803-info" class="comment-info"><span class="comment-age">(11 Feb '15, 10:01)</span> beastham</div></div><span id="39858"></span><div id="comment-39858" class="comment"><div id="post-39858-score" class="comment-score"></div><div class="comment-text"><p>The server logs show the following entries for OpenID:</p><hr /><p>[2015-02-11 20:35:22,886] WARN org.openid4java.consumer.AbstractNonceVerifier : Nonce is too old: 2015-02-11T08:27:20Zfur58z [2015-02-11 20:35:22,887] ERROR com.google.gerrit.httpd.auth.openid.OpenIdServiceImpl : OpenID failure: Nonce verification failed. Likely caused by clock skew on this server, install/configure NTP.</p><hr /><p>(NTP is up and synced. 2015-02-11T08:27:20Zfur58z doesn't appear to be valid ISO 8601, however.)</p><hr /><p>[2015-02-12 09:47:51,030] ERROR com.google.gerrit.httpd.auth.openid.OpenIdServic eImpl : Cannot discover OpenID http:// org.openid4java.discovery.DiscoveryException: 0x500: Cannot parse identifier: ht tp:// at org.openid4java.discovery.Discovery.parseIdentifier(Discovery.java:12 1) at org.openid4java.discovery.Discovery.discover(Discovery.java:129) at org.openid4java.consumer.ConsumerManager.discover(ConsumerManager.jav a:538) at com.google.gerrit.httpd.auth.openid.OpenIdServiceImpl.init(OpenIdServ iceImpl.java:523) at com.google.gerrit.httpd.auth.openid.OpenIdServiceImpl.discover(OpenId ServiceImpl.java:150) at com.google.gerrit.httpd.auth.openid.LoginForm.discover(LoginForm.java :164) at com.google.gerrit.httpd.auth.openid.LoginForm.doPost(LoginForm.java:1 54)</p><hr /><p>Would it be possible to use a different provider? Launchpad.net is probably your best bet at this point.</p><p>I hate to "solve" the issue that way but it's probably the easiest going forward. Gerrit has limited OpenID configuration options (i.e. enabling and disabling it). If the problem is on our side, fixing it likely involves recompiling Gerrit itself or openid4java. If it's a Wordpress.com issue I have no idea how feasible it would be to try to fix it.</p></div><div id="comment-39858-info" class="comment-info"><span class="comment-age">(13 Feb '15, 14:18)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-39802" class="comment-tools"></div><div class="clear"></div><div id="comment-39802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

