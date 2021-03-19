+++
type = "question"
title = "rpcapd allowed hosts list format in linux?"
description = '''I&#x27;m using rpcapd on my Tomato router to access all packets from a Wireshark client on my network. rpcapd works great and I can see traffic for each bridge I select in remote connection in Wireshark. I am using null authentication at the moment, and I would of course like to create an allowed hosts l...'''
date = "2013-05-18T23:34:00Z"
lastmod = "2013-05-20T07:26:00Z"
weight = 21256
keywords = [ "rpcapd", "list", "hosts", "winpcap", "allowed" ]
aliases = [ "/questions/21256" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [rpcapd allowed hosts list format in linux?](/questions/21256/rpcapd-allowed-hosts-list-format-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21256-score" class="post-score" title="current number of votes">0</div><span id="post-21256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using rpcapd on my Tomato router to access all packets from a Wireshark client on my network. rpcapd works great and I can see traffic for each bridge I select in remote connection in Wireshark. I am using null authentication at the moment, and I would of course like to create an allowed hosts lists with the: rpcapd -l allowed_host_list but for some reason no format I use in this list is accepted during the connection in Wireshark. I've tried IP address, MAC address, etc, every time it says the device I'm connecting from is not in the allowed hosts list. Any idea what the format is supposed to be for the allowed hosts list in linux? I see the format for rpcapd.ini in Windows, but can find no reference to what this file format should be in linux?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpcapd" rel="tag" title="see questions tagged &#39;rpcapd&#39;">rpcapd</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-allowed" rel="tag" title="see questions tagged &#39;allowed&#39;">allowed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '13, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/57a8b8437c22ed09e641de2e143a8253?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fvultee&#39;s gravatar image" /><p><span>fvultee</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fvultee has no accepted answers">0%</span></p></div></div><div id="comments-container-21256" class="comments-container"></div><div id="comment-tools-21256" class="comment-tools"></div><div class="clear"></div><div id="comment-21256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21310"></span>

<div id="answer-container-21310" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21310-score" class="post-score" title="current number of votes">1</div><span id="post-21310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any idea what the format is supposed to be for the allowed hosts list in linux?</p></blockquote><p>according to the (WinPcap) code, it is a file with a list of allowed hosts, separated by one of these characters.</p><pre><code>pcap-remote.h

#define RPCAP_HOSTLIST_SEP &quot; ,;\n\r&quot;</code></pre><p>According to the online help of rpcapd</p><pre><code>  -l &lt;host_list&gt;: a file that keeps the list of the hosts which are allowed
      to connect to this server (if more than one, list them one per line).
      We suggest to use literal names (instead of numeric ones) in order to
      avoid problems with different address families</code></pre><p>So far, so good...</p><blockquote><p>I've tried IP address, MAC address, etc, every time it says the device I'm connecting from is not in the allowed hosts list.</p></blockquote><p>Unfortunately the <strong>code</strong> to parse the hosts list is <strong>severely broken</strong>.</p><pre><code>int sock_check_hostlist(char *hostlist, const char *sep, struct sockaddr_storage *from, char *errbuf, int errbuflen)
{
    // checks if the connecting host is among the ones allowed
    if ( (hostlist) &amp;&amp; (hostlist[0]) )
    {
    char *token;                    // temp, needed to separate items into the hostlist
    struct addrinfo *addrinfo, *ai_next;
    char *temphostlist;

        temphostlist= (char *) malloc (strlen(hostlist) + 1);
        if (temphostlist == NULL)
        {
            sock_geterror(&quot;sock_check_hostlist(), malloc() failed&quot;, errbuf, errbuflen);
            return -2;
        }

        // The problem is that strtok modifies the original variable by putting &#39;0&#39; at the end of each token
        // So, we have to create a new temporary string in which the original content is kept
        strcpy(temphostlist, hostlist);

        token= strtok(temphostlist, sep);</code></pre><p>Instead of tokenizing the <strong>content</strong> of the file, it uses the <strong>file name</strong> :-(. Thus, you will never get a positive answer unless you name the hosts list file according to the connecting IP address ;-)</p><p>This works on my system.</p><blockquote><p><code>create an empty file named: 192.168.158.139,192.168.158.140,.txt</code></p></blockquote><p>Then start rpcapd.</p><blockquote><p><code>./rpcapd -b 192.168.158.129 -p 2002 -n -l 192.168.158.139,192.168.158.140,.txt</code><br />
</p></blockquote><p>Now connect from 192.168.158.139 or from 192.168.158.140.</p><p>The content of the file does not matter in this case, as it is not read anyways.</p><p>While this might be an acceptable workaround for you, it is clearly a bug and should be reported to the WinPcap team.</p><p>Please do so, with a reference to my answer.</p><blockquote><p><code>http://www.winpcap.org/bugs.htm</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '13, 07:40</strong> </span></p></div></div><div id="comments-container-21310" class="comments-container"></div><div id="comment-tools-21310" class="comment-tools"></div><div class="clear"></div><div id="comment-21310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

