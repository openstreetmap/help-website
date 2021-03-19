+++
type = "question"
title = "out-of-order arrived packets"
description = '''I have 2 client applications on c#, one is comercial with non-open-code, and one is mine. Both connect to the sever via tcp, and make simple stuff: get packet from server, analyze it, send another packet back to the server. I try to compare the speed, by running same time on one machine with same pr...'''
date = "2014-06-26T03:57:00Z"
lastmod = "2014-06-26T06:15:00Z"
weight = 34210
keywords = [ "tcpdump", "out-of-order", "packet" ]
aliases = [ "/questions/34210" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [out-of-order arrived packets](/questions/34210/out-of-order-arrived-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34210-score" class="post-score" title="current number of votes">0</div><span id="post-34210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 2 client applications on c#, one is comercial with non-open-code, and one is mine.</p><p>Both connect to the sever via tcp, and make simple stuff: get packet from server, analyze it, send another packet back to the server.</p><p>I try to compare the speed, by running same time on one machine with same priority. And get very strange thing:</p><p>Packet for mine application send first from the server, and a few us later a packet for commercial app is sent. But on the wireshark dump I see that first packet arrives later for 60-150 us then the second one.</p><p>Could you please be so kind to help me to find why? How wireshark messure the time for packet arrival? Could I somehow block the socket and make delays that's way?</p><p>Thank you in advance!</p><p>Socket part of the app:</p><pre><code> private Socket _socket;
    private byte[] _buffer;
    public void Start(IPEndPoint endpoint)
    {
        _buffer = new byte[1024];
        _socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp)
        {
            NoDelay = true,
            ReceiveBufferSize = 1024
        };
        _socket.Connect(endpoint);

        _socket.BeginReceive(_buffer, 0, _buffer.Length, SocketFlags.None, OnReceive, null);
    }

    private void OnReceive(IAsyncResult result)
    {
        var recieved = _socket.EndReceive(result);

        ProcessReceived(recieved);

        _socket.BeginReceive(_buffer, 0, _buffer.Length, SocketFlags.None, OnReceive, null);
    }

    private void ProcessReceived(int recieved)
    {
        // process received data
    }</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '14, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/3b3c4174707af1f6d3897af1191604ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rev3n&#39;s gravatar image" /><p><span>rev3n</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rev3n has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '14, 04:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34210" class="comments-container"><span id="34211"></span><div id="comment-34211" class="comment"><div id="post-34211-score" class="comment-score"></div><div class="comment-text"><p>We'll need some more info. Is there ARP going on? How did you measure transmit timings? Where did you measure the receive timings?</p></div><div id="comment-34211-info" class="comment-info"><span class="comment-age">(26 Jun '14, 05:37)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="34213"></span><div id="comment-34213" class="comment"><div id="post-34213-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I don't know what to answer you about ARP, it is tcp/ip over Ethernet connection via 10G line (machine - switch - server). About transmit timings, I did not measure it, server generate packets consistently, so I expect delay between them not more then 10s us. Receive timings I measured by WireShark.</p></div><div id="comment-34213-info" class="comment-info"><span class="comment-age">(26 Jun '14, 06:15)</span> <span class="comment-user userinfo">rev3n</span></div></div></div><div id="comment-tools-34210" class="comment-tools"></div><div class="clear"></div><div id="comment-34210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

